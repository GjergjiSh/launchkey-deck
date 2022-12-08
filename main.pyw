import argparse

from pygame.midi import MidiException
from launchpad.model.board import LaunchPad
import logging


def setup():
    # Set up the argument parser
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-loglevel",
        metavar="--loglevel",
        type=int,
        default=3,
        help="Loglevel [0,5]")

    args = parser.parse_args()

    # Set up logging
    filename = "%slog" % __file__[:-2]
    log_format = "{asctime} {levelname:<8} {message}"
    logging.basicConfig(
        level=args.loglevel * 10,
        format=log_format,
        style="{",
        handlers=[
            logging.FileHandler(filename),
            logging.StreamHandler()
        ]
    )


def open_launchpad(launchpad_name: bytes = b'Launchkey Mini MK3 MIDI'):
    # Init pygame.midi
    try:
        LaunchPad.startup()
    except MidiException as e:
        logging.error(e)

    # Wait for the device to be connected
    launchpad = LaunchPad.open(launchpad_name)
    launchpad.register_groups("./config.yml")

    return launchpad


def run(launchpad: LaunchPad):
    status = -1

    # Start the main loop
    try:
        launchpad.loop()
    except KeyboardInterrupt:
        logging.info("Exiting...")
        status = 0
    except Exception as ex:
        logging.error(f"Error occurred when processing the launchpad input {ex}")
        status = -1

    # Rerun if the status is not 0
    if status != 0:
        run(launchpad)


def main():
    setup()
    launchpad = open_launchpad()
    run(launchpad)
    LaunchPad.shutdown()


if __name__ == "__main__":
    main()
