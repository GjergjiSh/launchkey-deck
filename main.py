from launchpad.model.Launchpad import *


def main():
    launchpad = LaunchPad()
    try:
        launchpad.loop()
    except KeyboardInterrupt as ex:
        print("Exiting...")
        launchpad.deinit()


if __name__ == "__main__":
    main()
