import logging

import pygame.midi
from pygame.midi import MidiException


class EventEngine:
    device_id = -1
    midi_in = None

    def startup(self):
        pygame.midi.init()

        # Check if pygame.midi is initialized
        if not pygame.midi.get_init():
            raise Exception("Failed to initialize pygame.midi")

        # Get the default output device ID and initialize the midi input
        self.device_id = pygame.midi.get_default_input_id()

        # Check if the device is connected
        if self.device_id == -1:
            raise MidiException("No MIDI device found")

        self.midi_in = pygame.midi.Input(1)

        # Check if the midi input is initialized
        # TODO: Custom error handling
        if not self.midi_in:
            raise Exception("Failed to initialize midi input")

        # TODO: Check this
        # pygame.time.Clock()
        logging.info("Event engine initialized")

    # Note: Currently only one event at a time is supported
    def get_event(self, events_nr: int = 1) -> dict | None:
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

    def shutdown(self):
        pygame.midi.quit()
        logging.info("Event engine shutdown")
