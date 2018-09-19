import uuid
import json
from commander.commands.Command import Command
from commander.data_classes.Camera import Camera
from commander.executors.CameraExecutor import CameraExecutor


class AddCameraCommand(Command):
    """
    Add a camera command.
    """

    def __init__(self):
        Command.__init__(self)

    def execute(self, **kwargs):
        """
        Execute the command.

        :param kwargs: key-worded arguments.
        :keyword cameras: List of the cameras.
        :keyword stream_url: Video camera's URL.
        :return: Response.
        """
        cameras = kwargs.get('cameras')
        stream_url = kwargs.get('stream_url')

        id = str(uuid.uuid1()).replace("-", "")
        camera_executor = CameraExecutor()
        camera_executor.execute(stream_url=stream_url, namespace=id)

        if not camera_executor.is_running():
            return [json.dumps({"message": "Bad URL of the video stream.", "code": 422})]

        camera = Camera()
        camera.id = id
        camera.url = stream_url
        camera.executor = camera_executor

        cameras[id] = camera

        return [json.dumps({"message": "Camera is added.", "code": 200, "camera": camera.to_dict()})]
