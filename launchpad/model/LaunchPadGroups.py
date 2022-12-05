from launchpad.model.LaunchPadItems import Pads, Potentiometer, PlayRec, Keys
from launchpad.commands.CommandFactory import create_command
from launchpad.commands.Command import *
from enum import IntEnum


class LaunchPadItemGroup:
    group_code = None
    commands: dict[IntEnum, Command]

    # TODO -> Fix warning
    def consume_event(self, **event: dict):
        personal_code = event.get("personal_code")
        if personal_code in self.commands:
            self.commands[personal_code].execute(**event)


class PadGroup(LaunchPadItemGroup):
    group_code = 153

    def __init__(self, pad_config: dict):
        self.commands: dict[int, Command | None] = {}

        for pad in pad_config:
            self.commands.update(
                {pad.get("code"): create_command(pad.get("command"), **pad)}
            )


# TODO: Fix this -> Index out of range
class PotentiometerGroup(LaunchPadItemGroup):
    group_code = 176

    def __init__(self, potentiometer_config: dict):

        self.commands: dict[int, Command] = {
            # Potentiometer.POT1: SetVolumeCommand(),
            # Potentiometer.POT2: SetVolumeCommand(),
            # Potentiometer.POT3: SetVolumeCommand(),
            # Potentiometer.POT4: SetVolumeCommand(),
            # Potentiometer.POT5: SetVolumeCommand(),
            # Potentiometer.POT6: SetVolumeCommand(),
            # Potentiometer.POT7: SetVolumeCommand(),
            # Potentiometer.POT8: SetVolumeCommand(),
        }

        for potentiometer in potentiometer_config:
            self.commands.update(
                {potentiometer.get("code"): create_command(potentiometer.get("command"), **potentiometer)}
            )


class PlayRecGroup(LaunchPadItemGroup):
    group_code = 191

    def __init__(self, play_rec_config: dict):
        #dll_path = r"C:/Users/Gjergji/Repos/midi-controller/device-switcher/build/Release/OutputDeviceSwitcher.dll"
        self.commands: dict[PlayRec, Command] = {
            # PlayRec.PLAY: SwitchDeviceCommand(dll_path),
            # PlayRec.REC: KillProcessCommand("pythonw.exe"),
        }

        for play_rec in play_rec_config:
            self.commands.update(
                {play_rec.get("code"): create_command(play_rec.get("command"), **play_rec)}
            )


class KeysGroup(LaunchPadItemGroup):
    group_code = 144

    def __init__(self):
        self.commands: dict[Keys, Command] = {
            Keys.K1: UnimplementedCommand(),
            Keys.K2: UnimplementedCommand(),
            Keys.K3: UnimplementedCommand(),
            Keys.K4: UnimplementedCommand(),
            Keys.K5: UnimplementedCommand(),
            Keys.K6: UnimplementedCommand(),
            Keys.K7: UnimplementedCommand(),
            Keys.K8: UnimplementedCommand(),
            Keys.K9: UnimplementedCommand(),
            Keys.K10: UnimplementedCommand(),
            Keys.K11: UnimplementedCommand(),
            Keys.K12: UnimplementedCommand(),
            Keys.K13: UnimplementedCommand(),
            Keys.K14: UnimplementedCommand(),
            Keys.K15: UnimplementedCommand(),
            Keys.K16: UnimplementedCommand(),
            Keys.K17: UnimplementedCommand(),
            Keys.K18: UnimplementedCommand(),
            Keys.K19: UnimplementedCommand(),
            Keys.K20: UnimplementedCommand(),
            Keys.K21: UnimplementedCommand(),
            Keys.K22: UnimplementedCommand(),
            Keys.K23: UnimplementedCommand(),
            Keys.K24: UnimplementedCommand(),
            Keys.K25: UnimplementedCommand(),
        }
