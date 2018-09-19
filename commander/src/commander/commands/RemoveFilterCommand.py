import json
from commander.commands.Command import Command


class RemoveFilterCommand(Command):
    """
    Remove the filter of the camera command.
    """

    def __init__(self):
        Command.__init__(self)

    def execute(self, **kwargs):
        """
        Execute the command.

        :param kwargs: key-worded arguments.
        :keyword cameras: List of the cameras.
        :keyword camera_id: Camera's ID.
        :keyword filter_id: Filters's ID.
        :return: Response.
        """
        cameras = kwargs.get('cameras')
        camera_id = kwargs.get('camera_id')
        filter_id = kwargs.get('filter_id')

        if not camera_id in cameras:
            return [json.dumps({"message": "Camera with this ID does not exist.", "code:": 404})]

        if not filter_id in cameras[camera_id].filters:
            return [json.dumps({"message": "Filter with this ID does not exist.", "code:": 404})]

        cameras[camera_id].filters[filter_id].executor.stop()
        del cameras[camera_id].filters[filter_id]
        return [json.dumps({"message": "Filter is removed.", "code": 200})]
