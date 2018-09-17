import rospy


class Camera:
    """
    Camera class.

    :ivar id: Camera's ID.
    :ivar url: Camera's URL.
    :ivar executor: Executor of the camera.
    """

    def __init__(self):
        self.id = None
        self.url = None
        self.executor = None

    def set_id(self, id):
        """
        Set camera's ID.

        :param id: Camera's ID.
        """
        self.id = id

    def get_id(self):
        """
        Get camera's ID.

        :return: Camera's ID.
        """
        return self.id

    def set_url(self, url):
        """
        Set camera's URL.

        :param url: Camera's URL.
        """
        self.url = url

    def get_url(self):
        """
        Get camera's URL.

        :return: Camera's URL.
        """
        return self.url

    def set_executor(self, executor):
        """
        Set executor of the camera.

        :param executor: Executor of the camera.
        """
        self.executor = executor

    def get_executor(self):
        """
        Get executor of the camera.

        :return: Executor of the camera.
        """
        return self.executor

    def to_dict(self):
        """
        Camera object to dictionary.

        :return: Dictionary of the camera object.
        """
        return {
            "id": self.id,
            "url": self.url,
            "topics_list": rospy.get_published_topics(self.id)
        }
