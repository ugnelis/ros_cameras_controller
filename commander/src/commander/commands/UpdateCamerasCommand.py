from commander.commands.Command import Command


class CheckCamerasCommand(Command):
    """
    Check if cameras are alive.
    """

    def __init__(self):
        Command.__init__(self)

    def execute(self, **kwargs):
        """
        Execute the command.

        :param kwargs: key-worded arguments.
        :keyword cameras: List of the cameras.
        :return: Response.
        """
        cameras = kwargs.get('cameras')

        not_running_ids = [id for id in cameras if cameras[id].is_running() == False]

        for id in not_running_ids:
            del cameras[id]

        return ["Cameras have been checked."]
