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
        self.commands: dict[Pads, Command] = {
            # Top row
            Pads.T1: Cmd1(),
            Pads.T2: Cmd1(),
            Pads.T3: Cmd1(),
            Pads.T4: Cmd1(),
            Pads.T5: Cmd1(),
            Pads.T6: Cmd1(),
            Pads.T7: Cmd1(),
            Pads.T8: Cmd1(),
            # Bottom row
            Pads.B1: Cmd1(),
            Pads.B2: Cmd1(),
            Pads.B3: Cmd1(),
            Pads.B4: Cmd1(),
            Pads.B5: Cmd1(),
            Pads.B6: Cmd1(),
            Pads.B7: Cmd1(),
            Pads.B8: Cmd1(),
        }


class PotentiometerGroup(LaunchPadItemGroup):
    group_code = 176

    def __init__(self):
        self.commands: dict[Potentiometer, Command] = {
            Potentiometer.POT1: CMD2(),
            Potentiometer.POT2: CMD2(),
            Potentiometer.POT3: CMD2(),
            Potentiometer.POT4: CMD2(),
            Potentiometer.POT5: CMD2(),
            Potentiometer.POT6: CMD2(),
            Potentiometer.POT7: CMD2(),
            Potentiometer.POT8: CMD2(),
        }
