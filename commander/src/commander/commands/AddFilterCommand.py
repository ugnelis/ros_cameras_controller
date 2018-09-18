import uuid
import json
from commander.commands.Command import Command
from commander.data_classes.Filter import Filter
from commander.executors.ThresholdFilterExecutor import ThresholdFilterExecutor


class AddFilterCommand(Command):
    """
    Add a filter for the camera command.
    """

    def __init__(self):
        Command.__init__(self)

    def execute(self, **kwargs):
        """
        Execute the command.

        :param kwargs: key-worded arguments.
        :keyword cameras: List of the cameras.
        :keyword camera_id: Camera's ID.
        :keyword image_topic: Video camera's topic.
        :keyword filter_type: Filter type.
        :return: Response.
        """
        cameras = kwargs.get('cameras')
        camera_id = kwargs.get('camera_id')
        filter_type = kwargs.get('filter_type')

        if not camera_id in cameras:
            return [json.dumps({"message": "Camera with this ID does not exist.", "code": 404})]

        image_topic = "/" + camera_id + "/video_stream_to_topic/stream/image"

        id = str(uuid.uuid1()).replace("-", "")

        if filter_type == "threshold":
            filter_executor = ThresholdFilterExecutor()
            filter_executor.execute(image_topic=image_topic, namespace=id)
        else:
            return [json.dumps({"message": "Filter type does not exist.", "code": 404})]

        filter = Filter()
        filter.set_id(id)
        filter.set_executor(filter_executor)

        cameras[camera_id].add_filter(filter)

        return [json.dumps({"message": "Filter is added.", "code": 200, "camera": filter.to_dict()})]
