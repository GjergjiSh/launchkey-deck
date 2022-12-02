from launchpad.model.LaunchPadItems import Pads, Potentiometer, PlayRec
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
        self.commands: dict[Pads, Command] = {
            # Top row
            Pads.T1: UnimplementedCommand(),
            Pads.T2: UnimplementedCommand(),
            Pads.T3: UnimplementedCommand(),
            Pads.T4: UnimplementedCommand(),
            Pads.T5: UnimplementedCommand(),
            Pads.T6: UnimplementedCommand(),
            Pads.T7: UnimplementedCommand(),
            Pads.T8: UnimplementedCommand(),
            # Bottom row
            Pads.B1: OpenFolderCommand(r"C:\Users\Gjergji\Repos"),
            Pads.B2: OpenFolderCommand(r"C:\Users\Gjergji\Desktop"),
            Pads.B3: UnimplementedCommand(),
            Pads.B4: UnimplementedCommand(),
            Pads.B5: UnimplementedCommand(),
            Pads.B6: UnimplementedCommand(),
            Pads.B7: UnimplementedCommand(),
            Pads.B8: UnimplementedCommand(),
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


class PlayRecGroup(LaunchPadItemGroup):
    group_code = 191

    def __init__(self):
        dll_path = r"C:/Users/Gjergji/Repos/midi-controller/device-switcher/build/Release/OutputDeviceSwitcher.dll"
        self.commands: dict[PlayRec, Command] = {
            PlayRec.PLAY: SwitchDevice(dll_path),
            PlayRec.REC: KillProcessCommand("pythonw.exe"),
        }
