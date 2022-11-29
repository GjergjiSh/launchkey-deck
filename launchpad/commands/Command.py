from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError


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
