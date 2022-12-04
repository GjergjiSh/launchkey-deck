import pygame.midi
from pygame.midi import MidiException
import time

from launchpad.model.LaunchPadGroups import *


class LaunchPad:
    def __init__(self) -> None:
        # Get the default output device ID
        self.device_id = pygame.midi.get_default_input_id()

        # Check if the device is connected
        if self.device_id == -1:
            raise MidiException("No MIDI device found")

        self.midi_in = pygame.midi.Input(self.device_id)

        self.groups: dict[int, LaunchPadItemGroup] = {
            PadGroup.group_code: PadGroup(),
            PotentiometerGroup.group_code: PotentiometerGroup(),
            PlayRecGroup.group_code: PlayRecGroup(),
            KeysGroup.group_code: KeysGroup(),
        }

        logging.info("Launchpad initialized")

    # Note: Currently only one event at a time is supported
    def read_midi_event(self, events_nr: int = 1) -> dict | None:
        midi_events: list[list[list[int] | int]] = self.midi_in.read(events_nr)
        if midi_events:
            event = {
                "group_code": midi_events[0][0][0],
                "personal_code": midi_events[0][0][1],
                "value": midi_events[0][0][2]
            }
            logging.debug(f"Midi Event: {event}")
            return event

        logging.debug("No MIDI events found")
        return None

    def route_event(self, event: dict) -> None:
        group_code = event.get("group_code")
        if group_code in self.groups:
            self.groups[group_code].consume_event(**event)
        else:
            logging.debug(f"Group code {group_code} not found")

    def loop(self, clock_tick: int = 500):
        clock = pygame.time.Clock()
        while True:
            clock.tick(clock_tick)
            event = self.read_midi_event()
            if event:
                self.route_event(event)

    @staticmethod
    def startup():
        pygame.midi.init()

        # Check if pygame.midi is initialized
        if not pygame.midi.get_init():
            raise Exception("Failed to initialize pygame.midi")

    @staticmethod
    def get_connected_device_names() -> list[str]:
        connected_devices = []
        device_count = pygame.midi.get_count()

        for i in range(device_count):
            (interface, name, is_input, is_output, is_opened) = pygame.midi.get_device_info(i)
            connected_devices.append(name)

        return connected_devices

    @staticmethod
    def open(device_name: bytes):
        connected_device_names = LaunchPad.get_connected_device_names()

        while device_name not in connected_device_names:
            # Reinitialize pygame.midi to get the latest connected devices
            pygame.midi.quit()
            pygame.midi.init()
            connected_device_names = LaunchPad.get_connected_device_names()
            time.sleep(1)

        logging.info(f"{device_name} connected")
        return LaunchPad()

    @staticmethod
    def shutdown():
        pygame.midi.quit()
        logging.info("Launchpad disconnected")
