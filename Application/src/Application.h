#pragma once

#include "Appazoid/Appazoid.h"
#include "Layers/MainLayer.h"

class MyApplication :public az::Application
{
public:
	MyApplication();
	void MenubarCallback();
};
