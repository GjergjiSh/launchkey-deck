from launchpad.model.items import PlayRec, Keys, Pad, Potentiometer
from launchpad.commands.cmd import *


class LaunchPadItemGroup:
    group_code = None
    commands: dict[int, Command]

    # TODO -> Fix warning
    def consume_event(self, **event: dict):
        personal_code = event.get("personal_code")
        if personal_code in self.commands:
            self.commands[personal_code].execute(**event)


class PadGroup(LaunchPadItemGroup):
    group_code = 153

    def __init__(self, pad_config: dict):
        self.commands: dict[Pad, Command | None] = dict()

        for pad in pad_config:
            self.commands.update({
                pad.get("code"): create_command(**pad)
            })


# TODO: Fix this -> Index out of range
class PotentiometerGroup(LaunchPadItemGroup):
    group_code = 176

    def __init__(self, potentiometer_config: dict):
        self.commands: dict[Potentiometer, Command] = dict()

        for potentiometer in potentiometer_config:
            self.commands.update({
                potentiometer.get("code"): create_command(**potentiometer)
            })


class PlayRecGroup(LaunchPadItemGroup):
    group_code = 191

    def __init__(self, play_rec_config: dict):
        self.commands: dict[PlayRec, Command] = dict()

        for play_rec in play_rec_config:
            self.commands.update({
                play_rec.get("code"): create_command(**play_rec)
            })


class KeysGroup(LaunchPadItemGroup):
    group_code = 144

    def __init__(self, keys_config: dict):
        self.commands: dict[Keys, Command] = dict()

        for key in keys_config:
            self.commands.update({
                key.get("code"): create_command(**key)
                })
