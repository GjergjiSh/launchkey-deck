#pragma once

#include <stdio.h>
#include <wchar.h>
#include <tchar.h>
#include <vector>
#include <string>
#include <atlstr.h>
#include <fstream>
#include <iostream>

#include "windows.h"
#include "Mmdeviceapi.h"
#include "PolicyConfig.h"
#include "Propidl.h"
#include "Functiondiscoverykeys_devpkey.h"

IMMDeviceEnumerator *device_enumerator = NULL;
LPWSTR default_device_id = NULL;
IMMDevice *default_device = NULL;
IMMDeviceCollection *device_collection = NULL;
UINT device_count;

extern "C"
{

	__declspec(dllexport) struct WindowsAudioPlaybackDevice
	{
		std::wstring id;
		std::wstring name;
		BOOL is_default;
	};

	typedef void (*ProcessAudioPlaybackDeviceCallback)(LPWSTR, LPWSTR, BOOL);

	__declspec(dllexport) int init();
	__declspec(dllexport) int switch_device();
	__declspec(dllexport) void deinit();

	__declspec(dllexport) int set_output_device_by_id(std::wstring device_id);
	__declspec(dllexport) int get_active_device_id();
	__declspec(dllexport) int get_output_device_count();
	__declspec(dllexport) int refresh_output_devices_state();
}
