from abc import ABC, abstractmethod
import numpy as np
from enum import Enum, auto
import time
import pygame.midi

class LaunchPadItemTypes(Enum):
    PAD = "pad"
    POTENTIOMETER = "potentiometer"
    KEY = "key"
    SLIDER = "slider"
    BUTTON = "button"

class Command(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError

class LaunchPadItem:
    def __init__(self, group_code, personal_code, command : Command, type : LaunchPadItemTypes):
        self.group_code = group_code
        self.personal_code = personal_code
        self.values = np.arange(start=0, stop=127, step=1)
        self.command : Command = command
        self.type = type

class Cmd1(Command):
    def execute(self, **args):
        print('Pad')
        print(args.get("group_code"))
        print(args.get("personal_code"))
        print(args.get("value"))

class CMD2(Command):
    def execute(self, **args):
        print('Potentiometer')
        print(args.get("group_code"))
        print(args.get("personal_code"))
        print(args.get("value"))


class PadsGroup:
    group_code = 153
    def __init__(self):
        self.items : dict[int,Command] = {
            # Bottom row
            36: Cmd1(),
            37: Cmd1(),
            38: Cmd1(),
            39: Cmd1(),
            44: Cmd1(),
            45: Cmd1(),
            46: Cmd1(),
            47: Cmd1(),
            # Top row
            40: Cmd1(),
            41: Cmd1(),
            42: Cmd1(),
            43: Cmd1(),
            48: Cmd1(),
            49: Cmd1(),
            50: Cmd1(),
            51: Cmd1(),
        }

class PotentiometersGroup:
    group_code = 176
    def __init__(self):
        self.items : dict[int,Command] = {
            21: CMD2(),
            22: CMD2(),
            23: CMD2(),
            24: CMD2(),
            25: CMD2(),
            26: CMD2(),
            27: CMD2(),
            28: CMD2(),
        }


class LaunchPad:
    def __init__(self) -> None:
        pygame.midi.init()
        self.device_id = pygame.midi.get_default_input_id()
        self.midi_in = pygame.midi.Input(self.device_id)
        self.groups = {
            PadsGroup.group_code: PadsGroup(),
            PotentiometersGroup.group_code: PotentiometersGroup()
        }


    def read_midi_event(self, events_nr : int= 1) -> dict:
        midi_events = self.midi_in.read(events_nr)
        if midi_events:
            event = {
                "group_code" : midi_events[0][0][0],
                "personal_code" : midi_events[0][0][1],
                "value" : midi_events[0][0][2]
            }
            return event

        return None

    def trigger_command(self, event : dict) -> None:
        group_code = event.get("group_code")
        personal_code = event.get("personal_code")
        if group_code in self.groups:
            self.groups[group_code].items[personal_code].execute(**event)


    def loop(self, clock_tick : int = 500):
        going = True
        print ('Use ctrl+c to quit')
        clock = pygame.time.Clock()
        while going:
            clock.tick(clock_tick)
            event = self.read_midi_event()
            if event:
                self.trigger_command(event)

    def deinit(self):
        pygame.midi.quit()


if __name__ == "__main__":
    launchpad = LaunchPad()
    try:
        launchpad.loop()
    except KeyboardInterrupt as ex:
        print("exiting...")
        launchpad.deinit()