import argparse
import sys

from pygame.midi import MidiException

from launchpad.model.Launchpad import *


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


def run():
    status = -1
    # Wait for the device to be connected
    launchpad = LaunchPad.wait_for_device_connection()

    # Start the main loop
    try:
        launchpad.loop()
    except KeyboardInterrupt:
        logging.info("Exiting...")
        status = 0
    except RuntimeError as ex:
        logging.error(f"Failed to run command {ex}")
        status = -1
    except MidiException as ex:
        logging.error(f"Midi error {ex}")
        status = -1

    # Rerun if the status is not 0
    if status != 0:
        run()


def main():
    setup()

    # Startup
    #LaunchPad.startup()

    # Run
    run()

    # Deinitialize the launchpad
    LaunchPad.shutdown()


if __name__ == "__main__":
    main()
