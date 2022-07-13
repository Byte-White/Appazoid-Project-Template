#include "MainLayer.h"

void MainLayer::OnEvent(az::Event& e)
{
		az::EventDispatcher dispatcher(e);
		dispatcher.Dispatch<az::KeyReleasedEvent>(AZ_BIND_EVENT_FN(OnKeyReleased));
}

bool MainLayer::OnKeyReleased(az::KeyReleasedEvent& e)
{
		if (e.GetKeyCode() == az::Key::Escape)
		{
			//... do something ...
			APPAZOID_DEBUG("\'ESC\' Got Released");
		}
		return false;
}

void MainLayer::OnUIRender()
{
		ImGui::Begin("Main Window");
		ImGui::Text("Hello World!");
		ImGui::Button("Hi There!");
		ImGui::End();

		//Status 
		static bool show_info = true;
		static bool show_col_editor = false;

		ImGui::Begin("Status");
		ImGui::Checkbox("show info", &show_info);
		ImGui::SameLine();
		ImGui::Checkbox("show color editor", &show_col_editor);
		if (show_info)
		{
			ImGui::Text("Delta Time: %f", ImGui::GetIO().DeltaTime);
			ImGui::TextColored(ImVec4(1, 1, 0, 1), "Framerate: %.2f", ImGui::GetIO().Framerate);
		}

		if (show_col_editor)
		{
			ImGui::Begin("Color Editor");
			az::app->window_style.ColorEditor();
			ImGui::End();
		}
		ImGui::End();
}