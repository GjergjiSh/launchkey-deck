from launchpad.commands.cmd import Command

import logging
import os


class KillProcessCommand(Command):
    def __init__(self, **config: dict):
        self.process_name = config.get("process_name")

    def execute(self, **args):
        # Get the value of the event
        value = args.get("value")

        # Kill the process if the button was pressed
        if value > 0:
            try:
                os.system(f"TASKKILL /F /IM {self.process_name}")
            except WindowsError as e:
                logging.error(f"Failed to kill the process {self.process_name}", exc_info=True)
                raise e
