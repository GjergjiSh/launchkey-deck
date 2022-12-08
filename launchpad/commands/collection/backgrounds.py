from launchpad.commands.Command import Command

import ctypes
import struct
import os


class SwitchBackGroundCommand(Command):
    SPI_SETDESKWALLPAPER = 20

    def __init__(self, **config: dict):
        self.formal_mode = False
        self.background_path = str(config.get("casual_background_path"))
        self.formal_background_path = str(config.get("formal_background_path"))

    @property
    def is_64_windows(self):
        """Find out how many bits is OS. """
        return struct.calcsize('P') * 8 == 64

    def get_sys_parameters_info(self):
        """Based on if this is 32bit or 64bit returns correct version of SystemParametersInfo function. """
        return ctypes.windll.user32.SystemParametersInfoW if self.is_64_windows \
            else ctypes.windll.user32.SystemParametersInfoA

    def change_wallpaper(self):
        # Which wallpaper to use
        if self.formal_mode:
            wallpaper_path = self.formal_background_path
        else:
            wallpaper_path = self.background_path

        # Check if the wallpaper exists
        if not os.path.exists(wallpaper_path):
            raise FileNotFoundError("The wallpaper path does not exist")

        sys_parameters_info = self.get_sys_parameters_info()
        r = sys_parameters_info(self.SPI_SETDESKWALLPAPER, 0, wallpaper_path, 3)

        # When the SPI_SETDESKWALLPAPER flag is used,
        # SystemParametersInfo returns TRUE
        # unless there is an error (like when the specified file doesn't exist).
        if not r:
            raise(ctypes.WinError())

        # Switch the mode
        self.formal_mode = not self.formal_mode

    # def switch_mode(self):
    #     logging.info("Switching background mode")
    #     print("Switching background mode")
    #     if self.formal_mode:
    #         ctypes.windll.user32.SystemParametersInfoW(20, 0, self.background_path, 0)
    #     else:
    #         ctypes.windll.user32.SystemParametersInfoW(20, 0, self.formal_background_path, 0)
    #     self.formal_mode = not self.formal_mode
    #     print(f"Formal mode: {self.formal_mode}")

    def execute(self, **args):
        # Check if the background exists
        if not os.path.exists(self.background_path):
            raise FileNotFoundError("The background path does not exist")

        # Get the value of the event
        value = args.get("value")

        # Change the background if the button was pressed
        if value > 0:
            self.change_wallpaper()
            print(f"Formal mode: {self.formal_mode}")