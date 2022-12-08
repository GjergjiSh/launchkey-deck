from launchpad.commands.cmd import Command
from pycaw.pycaw import AudioUtilities

import logging
import os
import ctypes


class SetVolumeCommand(Command):
    def __init__(self, **config: dict):
        pass

    def execute(self, **args):
        # Get the available audio sessions
        sessions = [session for session in AudioUtilities.GetAllSessions() if session.Process]

        # Return if there are no sessions
        if not sessions:
            logging.warning("No audio sessions found")
            return

        # Log the available audio sessions
        for session in sessions:
            logging.debug(f"Session: {session.Process.name()}")

        # Get the session corresponding to the id of the potentiometer
        # Values for the potentiometer codes range from 21 to 28,
        # so we subtract 21 to get the index
        personal_code = args.get("personal_code")
        session_idx = personal_code - 21

        # log the potentiometer id and the corresponding session
        logging.debug(f"Potentiometer: {personal_code} - {session_idx}")

        # Return if the session index is out of range
        if session_idx < 0 or session_idx >= len(sessions):
            raise IndexError("The audio session index is out of range")

        # Get the interface of the closest session
        closest_session_interface = sessions[session_idx].SimpleAudioVolume
        # Set the volume of the closest session
        value = float(args.get("value")) / 127
        closest_session_interface.SetMasterVolume(value, None)

        # Log the volume change and the session name
        logging.debug(f"Volume set to {value} for {sessions[session_idx].Process.name()}")


class SwitchDeviceCommand(Command):
    def __init__(self, **config: dict):
        dll_path = str(config.get("dll_path"))

        # Check if the dll path exists
        if not os.path.exists(dll_path):
            raise FileNotFoundError("The dll for the device switcher library was not found")

        # Load the DLL
        try:
            self.device_switcher = ctypes.cdll.LoadLibrary(dll_path)
            # Log the success
            logging.info(f"Loaded the device switcher library from {dll_path}")
        except WindowsError as e:
            raise e

        # Initialize the Device Switcher
        if self.device_switcher.init() != 0:
            raise Exception("Failed to initialize the device switcher library")

        # # Unload the DLL when the program exits
        # atexit.register(self.device_switcher.deinit)

    def __del__(self):
        # Deinitialize the device switcher
        self.device_switcher.deinit()

    def execute(self, **args):
        # Get the value of the event
        value = args.get("value")
        # Switch the device if the value is larger than 0
        if value > 0:
            if self.device_switcher.switch_device() != 0:
                raise Exception("Failed to switch the device")
