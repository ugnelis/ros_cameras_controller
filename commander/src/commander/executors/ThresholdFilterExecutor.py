import rospy
import rospkg
import time
from commander.executors.Executor import Executor
from commander.utils.Process import Process


class ThresholdFilterExecutor(Executor):
    """
    Executor class for adding and removing camera.
    """

    def __init__(self):
        Executor.__init__(self)

    def execute(self, **kwargs):
        """
        Execute the command.

        :param kwargs: key-worded arguments.
        :keyword stream_url: Video stream's URL.
        :keyword namespace: Camera's namespace.
        """
        image_topic = kwargs.get('image_topic', "/video_stream_to_topic/stream/image")
        namespace = kwargs.get('namespace', "/")

        # Stop process if it's running.
        if self.process is not None:
            self.stop()

        rospack = rospkg.RosPack()
        file_path = rospack.get_path(
            'image_processing_filters') + "/launch/threshold_filter.launch"
        args_list = ['roslaunch', file_path, "image_raw:=%s" % image_topic]
        env = {'ROS_NAMESPACE': namespace}

        # Create and launch process.
        self.process = Process.create(*args_list, env=env)

        # Be sure that topics are running.
        while not rospy.get_published_topics(namespace):
            time.sleep(0.5)

    def stop(self):
        """
        Stop executors.
        """
        if self.process is not None:
            self.process = Process.terminate(self.process)

    def is_running(self):
        """
        Check if executor is running.

        :return: True if it's running, False if not.
        """
        return Process.is_running(self.process)
