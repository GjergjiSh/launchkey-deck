from launchpad.commands.cmd import Command
import datetime


class OpenFolderCommand(Command):
    def __init__(self, **config: dict):
        self.folder_path = str(config.get("folder_path"))
        self.t0 = -1
        self.t1 = -1

    def execute(self, **args):
        # Check if the folder exists
        if not os.path.exists(self.folder_path):
            raise FileNotFoundError("The folder path does not exist")

        # Get the value of the event
        value = args.get("value")

        # Start the timer if the button was pressed
        if value > 0:
            self.t0 = datetime.datetime.now()

        # Open the folder in the explorer or cmd if the button was released
        else:
            # Get the current time
            self.t1 = datetime.datetime.now()

            # Calculate the elapsed time in milliseconds
            elapsed_ms = int((self.t1 - self.t0).total_seconds() * 1000)

            # Check if the button has been pressed for more than 0.5 seconds
            if elapsed_ms > 500:
                # Open the folder in a terminal
                os.system(f"start cmd /k cd {self.folder_path}")
            else:
                os.startfile(self.folder_path)

            # Reset the pressed time
            self.t0 = -1
            self.t1 = -1