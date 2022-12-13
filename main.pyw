from launchpad.board import *
from launchpad.events.event_engine import *
from launchpad.common.utils import *


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


# def open_launchpad(launchpad_name: bytes = b'Launchkey Mini MK3 MIDI'):
#     # Init pygame.midi
#     try:
#         #startup()
#         launchpad = LaunchPad.open(launchpad_name)
#         launchpad.register_groups("./config.yml")
#         return launchpad
#     except MidiException as e:
#         logging.error(e, exc_info=True)


# def run(launchpad: LaunchPad):
#     status = -1
#
#     # Start the main loop
#     try:
#         launchpad.loop()
#     except KeyboardInterrupt:
#         logging.info("Exiting...")
#         status = 0
#     except Exception as ex:
#         logging.error(f"Error occurred when processing the launchpad input {ex}")
#         status = -1
#
#     # Rerun if the status is not 0
#     if status != 0:
#         run(launchpad)


def main():
    args = init_args()
    init_logging(args)

    event_engine = EventEngine()
    launchpad = LaunchPad()

    try:
        cfg = read_config("./config.yml")
    except Exception as ex:
        logging.error(ex, exc_info=True)
        return -1

    launchpad.register_groups(cfg)

    try:
        event_engine.startup()
    except Exception as ex:
        logging.error(ex, exc_info=True)

    while True:
        try:
            event = event_engine.get_event()
            if event:
                launchpad.process_event(event)
        except KeyboardInterrupt:
            logging.info("Exiting...")
            break
        # except Exception as ex:
        #     logging.error(f"Error occurred when processing the launchpad input {ex}")
        #     break

    event_engine.shutdown()
    return 0

    # launchpad = open_launchpad()
    # run(launchpad)


if __name__ == "__main__":
    main()
