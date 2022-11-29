import pygame.midi

from launchpad.model.LaunchPadGroups import *


class LaunchPad:
    def __init__(self) -> None:
        pygame.midi.init()
        self.device_id = pygame.midi.get_default_input_id()
        self.midi_in = pygame.midi.Input(self.device_id)
        self.groups: dict[int, LaunchPadItemGroup] = {
            PadGroup.group_code: PadGroup(),
            PotentiometerGroup.group_code: PotentiometerGroup()
        }

    def read_midi_event(self, events_nr: int = 1) -> dict | None:
        midi_events: list[list[list[int] | int]] = self.midi_in.read(events_nr)
        if midi_events:
            event = {
                "group_code": midi_events[0][0][0],
                "personal_code": midi_events[0][0][1],
                "value": midi_events[0][0][2]
            }
            return event

        return None

    def route_event(self, event: dict) -> None:
        group_code = event.get("group_code")
        if group_code in self.groups:
            self.groups[group_code].consume_event(**event)

    def loop(self, clock_tick: int = 500):
        clock = pygame.time.Clock()
        while True:
            clock.tick(clock_tick)
            event = self.read_midi_event()
            if event:
                self.route_event(event)

    def deinit(self):
        pygame.midi.quit()
