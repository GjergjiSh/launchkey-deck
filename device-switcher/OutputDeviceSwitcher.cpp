#include "OutputDeviceSwitcher.h"

int active_device_idx = -1;
int total_device_count = -1;

int init()
{
	_CrtSetReportMode(_CRT_ASSERT, 0);
	if (!SUCCEEDED(CoInitialize(NULL)))
		return -1;

	if (!SUCCEEDED(CoCreateInstance(__uuidof(MMDeviceEnumerator),
		NULL,
		CLSCTX_ALL,
		__uuidof(IMMDeviceEnumerator),
		(void**)&device_enumerator)))
		return -1;

	if (refresh_output_devices_state() != 0)
		return -1;

	get_active_device_id();

	return 0;
}

int switch_device()
{
	if (total_device_count == -1)
		return -1;

	active_device_idx = (active_device_idx + 1) % total_device_count;


	IMMDevice* device;
	if (!SUCCEEDED(device_collection->Item(active_device_idx, &device)))
		return -1;

	LPWSTR device_id = NULL;
	auto res = device->GetId(&device_id);
	if (!SUCCEEDED(res))
		return -1;

	return set_output_device_by_id(device_id);
}

void deinit()
{
	default_device->Release();
	device_collection->Release();
	device_enumerator->Release();
}

int set_output_device_by_id(std::wstring device_id)
{
	IPolicyConfigVista* policy_config = nullptr;
	ERole reserved = eConsole;

	// COCREATEINSTANCE CALLED AGAIN MIGHT NEED TO REFRESH DEVICES AFTERALL
	if (!SUCCEEDED(CoCreateInstance(__uuidof(CPolicyConfigVistaClient),
		NULL,
		CLSCTX_ALL,
		__uuidof(IPolicyConfigVista),
		(LPVOID*)&policy_config)))
		return -1;

	if (!SUCCEEDED(policy_config->SetDefaultEndpoint(device_id.c_str(), reserved)))
		return -1;

	policy_config->Release();
	return 0;
}


int refresh_output_devices_state()
{
	if (!SUCCEEDED(device_enumerator->GetDefaultAudioEndpoint(eRender,
		eMultimedia,
		&default_device)))
		return -1;

	if (!SUCCEEDED(default_device->GetId(&default_device_id)))
		default_device_id = NULL;

	if (!SUCCEEDED(device_enumerator->EnumAudioEndpoints(eRender, DEVICE_STATE_ACTIVE, &device_collection)))
		return -1;

	get_output_device_count();

	return 0;
}



int get_output_device_count()
{
	device_collection->GetCount(&device_count);
	total_device_count = device_count;
	return device_count;
}


int get_active_device_id()
{
	if (total_device_count == -1)
		return -1;

	IMMDevice* device;
	IPropertyStore* property_store;
	BOOL is_default;
	LPWSTR device_id;

	for (int i = 0; i < total_device_count; i++)
	{
		if (!SUCCEEDED(device_collection->Item(i, &device)))
			return -1;

		if (!SUCCEEDED(device->GetId(&device_id)))
			return -1;

		is_default = wcscmp(device_id, default_device_id) == 0;
		if (is_default)
		{
			active_device_idx = i;
			return i;
		}
	}

	property_store->Release();
	device->Release();
	return -1;
}