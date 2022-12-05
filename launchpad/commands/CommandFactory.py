from launchpad.commands.Command import *
from abc import ABC, abstractmethod


def create_command(command_name: str, **args: dict) -> Command:
    factories = {
        "TestCommand": TestCommandFactory(),
        "SetVolumeCommand": SetVolumeCommandFactory(),
        "SwitchDeviceCommand": SwitchDeviceCommandFactory(),
        "KillProcessCommand": KillProcessCommandFactory(),
        "OpenFolderCommand": OpenFolderCommandFactory(),
    }

    if command_name in factories:
        return factories[command_name].create(**args)
    else:
        raise Exception(f"Command {command_name} not found or supported")


class CommandFactory(ABC):
    @abstractmethod
    def create(self, **args: dict) -> Command:
        raise NotImplementedError


class TestCommandFactory(CommandFactory):
    def create(self, **args: dict) -> Command:
        return TestCommand(**args)


class SetVolumeCommandFactory(CommandFactory):
    def create(self, **args: dict) -> Command:
        return SetVolumeCommand(**args)


class SwitchDeviceCommandFactory(CommandFactory):
    def create(self, **args: dict) -> Command:
        return SwitchDeviceCommand(**args)


class KillProcessCommandFactory(CommandFactory):
    def create(self, **args: dict) -> Command:
        return KillProcessCommand(**args)


class OpenFolderCommandFactory(CommandFactory):
    def create(self, **args: dict) -> Command:
        return OpenFolderCommand(**args)
