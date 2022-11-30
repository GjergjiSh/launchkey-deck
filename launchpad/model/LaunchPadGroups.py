from launchpad.model.LaunchPadItems import Pads, Potentiometer
from launchpad.commands.CommandFactory import create_command
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

    # Pads.T1: create_command(next(iter(args.get(str(Pads.T1)))), **args),
    def __init__(self, **args: dict):
        self.commands: dict[Pads, Command] = {
            # Top row
            Pads.T1: SwitchDevice(),
            Pads.T2: SwitchDevice(),
            Pads.T3: SwitchDevice(),
            Pads.T4: SwitchDevice(),
            Pads.T5: SwitchDevice(),
            Pads.T6: SwitchDevice(),
            Pads.T7: SwitchDevice(),
            Pads.T8: SwitchDevice(),
            # Bottom row
            Pads.B1: SwitchDevice(),
            Pads.B2: SwitchDevice(),
            Pads.B3: SwitchDevice(),
            Pads.B4: SwitchDevice(),
            Pads.B5: SwitchDevice(),
            Pads.B6: SwitchDevice(),
            Pads.B7: SwitchDevice(),
            Pads.B8: SwitchDevice(),
        }


class PotentiometerGroup(LaunchPadItemGroup):
    group_code = 176

    def __init__(self, **args: dict):
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
