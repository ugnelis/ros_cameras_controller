import uuid
import json
from commander.commands.Command import Command
from commander.data_classes.Filter import Filter


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
        :keyword filter_types: List of the filter types.
        :keyword camera_id: Camera's ID.
        :keyword image_topic: Video camera's topic.
        :keyword filter_type: Filter type.
        :return: Response.
        """
        cameras = kwargs.get('cameras')
        filter_types = kwargs.get('filter_types')
        camera_id = kwargs.get('camera_id')
        filter_type = kwargs.get('filter_type')

        if not camera_id in cameras:
            return [json.dumps({"message": "Camera with this ID does not exist.", "code": 404})]

        image_topic = "/" + camera_id + "/video_stream_to_topic/stream/image"

        id = str(uuid.uuid1()).replace("-", "")

        if not filter_type in filter_types:
            return [json.dumps({"message": "Filter type does not exist.", "code": 404})]

        # Run filter.
        filter_executor = filter_types[filter_type]()
        filter_executor.execute(image_topic=image_topic, namespace=id)

        filter = Filter()
        filter.id = id
        filter.type = filter_type
        filter.executor = filter_executor

        cameras[camera_id].add_filter(filter)

        return [json.dumps({"message": "Filter is added.", "code": 200, "camera": filter.to_dict()})]
