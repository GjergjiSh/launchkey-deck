from launchpad.model.LaunchPadItems import Pads, Potentiometer
from launchpad.commands.Command import *
from enum import IntEnum


class LaunchPadItemGroup:
    group_code = None
    commands: dict[IntEnum, Command]

    def consume_event(self, **event: dict):
        personal_code = event.get("personal_code")
        if personal_code in self.commands:
            self.commands[personal_code].execute(**event)


class PadGroup(LaunchPadItemGroup):
    group_code = 153

    def __init__(self):
        dll_path = "C:/Users/Gjergji/Repos/midi-controller/device-switcher/build/Release/OutputDeviceSwitcher.dll"
        self.commands: dict[Pads, Command] = {
            # Top row
            Pads.T1: SwitchDevice(dll_path),
            Pads.T2: SwitchDevice(dll_path),
            Pads.T3: SwitchDevice(dll_path),
            Pads.T4: SwitchDevice(dll_path),
            Pads.T5: SwitchDevice(dll_path),
            Pads.T6: SwitchDevice(dll_path),
            Pads.T7: SwitchDevice(dll_path),
            Pads.T8: SwitchDevice(dll_path),
            # Bottom row
            Pads.B1: SwitchDevice(dll_path),
            Pads.B2: SwitchDevice(dll_path),
            Pads.B3: SwitchDevice(dll_path),
            Pads.B4: SwitchDevice(dll_path),
            Pads.B5: SwitchDevice(dll_path),
            Pads.B6: SwitchDevice(dll_path),
            Pads.B7: SwitchDevice(dll_path),
            Pads.B8: SwitchDevice(dll_path),
        }


class PotentiometerGroup(LaunchPadItemGroup):
    group_code = 176

    def __init__(self):
        self.commands: dict[Potentiometer, Command] = {
            Potentiometer.POT1: SetVolumeCommand(),
            Potentiometer.POT2: SetVolumeCommand(),
            Potentiometer.POT3: SetVolumeCommand(),
            Potentiometer.POT4: SetVolumeCommand(),
            Potentiometer.POT5: SetVolumeCommand(),
            Potentiometer.POT6: SetVolumeCommand(),
            Potentiometer.POT7: SetVolumeCommand(),
            Potentiometer.POT8: SetVolumeCommand(),
        }
