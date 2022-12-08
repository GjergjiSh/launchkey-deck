from launchpad.commands.cmd import Command


class TestCommand(Command):
    def __init__(self, **args: dict):
        self.message = args.get("message")
        self.output = args.get("output")
        # print(f"Test command initialized with {self.message}, {self.output}")

    def execute(self, **event):
        print(f"Test command: {self.message}, {self.output}")
