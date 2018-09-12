import json
from commander.commands.Command import Command


class UnknownCommand(Command):
    """
    Unknown command.
    """

    def __init__(self):
        Command.__init__(self)

    def execute(self, **kwargs):
        """
        Execute the command.
        :return: Response.
        """
        return [json.dumps({"message": "Command is unknown.", "code": 404})]
