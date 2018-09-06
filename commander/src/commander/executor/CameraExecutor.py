import rospy
import rospkg
import time
from commander.executor.Executor import Executor
from commander.utils.Process import Process


class CameraExecutor(Executor):
    """
    Executor class for adding and removing camera.
    """

    def __init__(self):
        Executor.__init__(self)

    def execute(self, **kwargs):
        """
        Execute the command.

        :param kwargs: key-worded arguments.
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

        # Be sure that topics are running.
        while not rospy.get_published_topics(namespace):
            time.sleep(0.5)

    def stop(self):
        """
        Stop executor.
        """
        if self.process is not None:
            self.process = Process.terminate(self.process)
