#pragma once
#include "Appazoid/Appazoid.h"


class MainLayer : public az::Layer
{

public:
	MainLayer()
	{

	}

	void OnConstruction() override
	{

	}

	void OnEvent(az::Event& e) override;

	bool OnKeyReleased(az::KeyReleasedEvent& e);

	void OnUIRender() override;
};