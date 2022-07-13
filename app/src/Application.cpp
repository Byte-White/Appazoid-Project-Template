#include "Application.h"
	MyApplication::MyApplication()
	{
		az::WindowStyle style;
		style.size = az::GetMonitorResolution() - 500;
		//style.monitor = glfwGetPrimaryMonitor(); //Fullscreen
		style.title = "Appazoid Application";
		style.stylecolor = az::StyleColor::StyleColorDark;

		//Enable Flags
		AddConfigFlagCallback([](ImGuiIO& io)
			{
				az::EnableConfigFlag(io, ImGuiConfigFlags_DockingEnable);
				az::EnableConfigFlag(io, ImGuiConfigFlags_NavEnableKeyboard);
				//az::EnableConfigFlag(io,ImGuiConfigFlags_ViewportsEnable);//Errors when using viewports
			});
		//Menu Callback
		
		AddMenubarCallback(AZ_BIND_CALLBACK_FN(MenubarCallback));
		AddLayer<MainLayer>("main_layer");
		az::AppazoidSpecification::Print();
		az::MemoryTracker::Print();
		Create(style);
	}

	void MyApplication::MenubarCallback()
	{
		if (ImGui::BeginMenu("File"))
		{
			if (ImGui::MenuItem("Exit"))this->Close();
			ImGui::EndMenu();
		}
	}




az::Application* az::CreateApplication(int argc, char** argv)
{
	return new MyApplication();
}
