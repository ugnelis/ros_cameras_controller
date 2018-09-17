import json
import rospy
from commander.commands.Command import Command
from commander.data_classes.Camera import Camera


class GetCamerasListCommand(Command):
    """
    Get the list of the cameras command.
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

        cameras_list = []

        for key in cameras.keys():
            # Add to the cameras list.
            cameras_list.append(cameras[key].to_dict())

        return [json.dumps({"cameras": cameras_list, "code": 200})]
