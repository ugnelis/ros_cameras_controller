import json
from commander.commands.Command import Command


class GetFilterTypesCommand(Command):
    """
    Get filters types command.
    """

    def __init__(self):
        Command.__init__(self)

    def execute(self, **kwargs):
        """
        Execute the command.

        :param kwargs: key-worded arguments.
        :keyword filter_types: List of the filter types.
        :return: Response.
        """
        filter_types = kwargs.get('filter_types')

        filter_types_list = []
        for key in filter_types:
            print(key)
            filter_types_list.append(key)

        return [json.dumps({"filter_types": filter_types_list, "code": 200}) ]
