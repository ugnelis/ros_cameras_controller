import os
import rospy
import rospkg
from commander.Command import Command
from commander.Process import Process


class AddCameraCommand(Command):
    """
    Command class for adding camera.
    """

    def execute(self, **kwargs):
        """
        Execute command.

        Args:
            kwargs: key-worded arguments.
        """
        stream_url = kwargs.pop('stream_url', "https://localhost:mjpg/video.mjpg")
        namespace = kwargs.pop('namespace', "/")

        # Stop process if it's running.
        if self.process is not None:
            self.stop()

        rospack = rospkg.RosPack()
        file_path = rospack.get_path(
            'video_stream_to_topic') + "/launch/video_stream_to_topic.launch"
        args_list = ['roslaunch', file_path, "stream_url:=%s" % stream_url]
        env = {'ROS_NAMESPACE': namespace}

        # Create and launch process.
        self.process = Process.create(*args_list, env=env)

    def stop(self):
        """
        Stop command.
        """
        if self.process is not None:
            self.process = Process.terminate(self.process)
