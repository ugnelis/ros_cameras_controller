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
        self.filters = {}

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

    def add_filter(self, filter):
        """
        Set camera's filter.

        :param filter: Camera's filter.
        """
        id = filter.get_id()
        if id in self.filters:
            raise ValueError("Filter with this ID already exists.")

        self.filters[id] = filter

    def remove_filter(self, id):
        """
        Remove filter.

        :param id: Filter's ID
        """
        del self.filters[id]

    def get_filters(self):
        """
        Get camera's filters.

        :return: Camera's filter.
            """
        return self.filters

    def to_dict(self):
        """
        Camera object to dictionary.

        :return: Dictionary of the camera object.
        """
        filters_list = []

        for key in self.filters.keys():
            # Add to the cameras list.
            filters_list.append(self.filters[key].to_dict())

        return {
            "id": self.id,
            "url": self.url,
            "filters": filters_list,
            "topics_list": rospy.get_published_topics(self.id)
        }
