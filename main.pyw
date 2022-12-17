from launchpad.board import *
from launchpad.events.event_engine import *
from launchpad.common.utils import *


def main():
    # Parse the arguments
    args = init_args()

    # Configure logging
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

    # Parse the commands config file
    try:
        cfg = read_config("commands.yml")
    except Exception as ex:
        logging.error(ex, exc_info=True)
        return -1

    # Create the and initialize the event engine
    event_engine = EventEngine()
    try:
        event_engine.startup()
    except Exception as ex:
        logging.error(ex, exc_info=True)
        return -1

    # Create and initialize the board
    launchpad = LaunchPad()
    launchpad.register_groups(cfg)

    # Limit the event reading and processing rate
    clock = pygame.time.Clock()
    event_rate = args.eventrate

    # Read and process the events
    while True:
        clock.tick(event_rate)
        try:
            event = event_engine.get_event()
            if event:
                launchpad.process_event(event)
        except KeyboardInterrupt:
            logging.info("Exiting...")
            break
        except Exception as ex:
            logging.error(f"Error occurred when processing the launchpad input {ex}", exc_info=True)
            break

    # Shutdown the event engine
    event_engine.shutdown()
    return 0


if __name__ == "__main__":
    main()
