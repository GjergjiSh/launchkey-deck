from abc import ABC, abstractmethod

import logging
import importlib


class Command(ABC):
    @abstractmethod
    def execute(self, **event: dict):
        raise NotImplementedError


def create_command(**kwargs: dict) -> Command:
    """ Create a command from the given arguments
        The arguments must contain the following
         - command_name: The name of the command to create
         - command_module: The module containing the command """

    # Get the command name and module from the args
    command_module = str(kwargs.get("command_module"))
    command_name = str(kwargs.get("command_name"))

    # Check if the command module and name are provided
    if command_module is None:
        raise Exception("Command module not specified")
    if command_name is None:
        raise Exception("Command name not specified")

    # Import the command module
    command_collection_module = importlib.import_module(
        f"launchpad.commands.collection.{command_module}"
    )

    return getattr(command_collection_module, command_name)(**kwargs)
