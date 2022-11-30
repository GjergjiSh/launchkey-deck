from abc import ABC, abstractmethod
from launchpad.commands.Command import *


class CommandFactory(ABC):
    @abstractmethod
    def create(self, **args):
        raise NotImplementedError


class SwitchDeviceCommandFactory(CommandFactory):
    def create(self, **args):
        return SwitchDevice(**args)


class SetVolumeCommandFactory(CommandFactory):
    def create(self, **args):
        return SetVolumeCommand(**args)


def create_command(command_type: str, **args):
    factories = {
        "switch_device": SwitchDeviceCommandFactory(),
        "set_volume": SetVolumeCommandFactory()
    }

    if command_type in factories:
        return factories[command_type].create(**args)
