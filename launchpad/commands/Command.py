from abc import ABC, abstractmethod
from pycaw.pycaw import AudioUtilities
import numpy as np


class Command(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError


class SetVolumeCommand(Command):
    def execute(self, **args):
        # Get the available audio sessions
        sessions = [session for session in AudioUtilities.GetAllSessions() if session.Process]

        # Return if there are no sessions
        if not sessions:
            return

        # Get the session corresponding to the id of the potentiometer
        personal_code = args.get("personal_code")
        session_idx = personal_code - 21

        # Return if the session index is out of range
        if session_idx < 0 or session_idx >= len(sessions):
            return

        # Get the interface of the closest session
        closest_session_interface = sessions[session_idx].SimpleAudioVolume
        # Set the volume of the closest session
        value = float(args.get("value")) / 127
        volume = closest_session_interface.SetMasterVolume(value, None)


class Cmd1(Command):
    def execute(self, **args):
        print('Pad')
        print(args.get("group_code"))
        print(args.get("personal_code"))
        print(args.get("value"))


class CMD2(Command):
    def execute(self, **args):
        print('Potentiometer')
        print(args.get("group_code"))
        print(args.get("personal_code"))
        print(args.get("value"))
