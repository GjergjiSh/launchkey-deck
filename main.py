import argparse
import sys

from launchpad.model.Launchpad import *


def main():
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

    # Initialize the launchpad
    try:
        launchpad = LaunchPad()
        status = 0
    except Exception as e:
        status = -1
        logging.error(f"Failed to initialize the launchpad: {e}")
        sys.exit(status)

    # Start the main loop
    try:
        launchpad.loop()
    except KeyboardInterrupt:
        logging.info("Exiting...")
        status = 0
    except RuntimeError as ex:
        logging.error(f"Failed to run command {ex}")
        status = -1

    # Deinitialize the launchpad
    launchpad.deinit()
    sys.exit(status)


if __name__ == "__main__":
    main()
