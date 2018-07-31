import rospy
import rospkg
from commander.Command import Command
from commander.Process import Process


class AddCameraCommand(Command):
    """
    Command class for adding camera.
    """

    def execute(self, argument):
        """
        Execute command.

        Args:
            argument: argument.
        """
        # Stop process if it's running.
        if self.process is not None:
            self.stop()

        rospack = rospkg.RosPack()
        file_path = rospack.get_path(
            'video_stream_to_topic') + "/launch/video_stream_to_topic.launch"
        args_list = ['roslaunch', file_path, "stream_url:=%s" % argument]

        # Create and launch process.
        self.process = Process.create(*args_list)

    def stop(self):
        """
        Stop command.
        """
        if self.process is not None:
            self.process = Process.terminate(self.process)
