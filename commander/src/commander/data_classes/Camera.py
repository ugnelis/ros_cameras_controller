import rospy


class Camera:
    """
    Camera class.

    :ivar id: Camera's ID.
    :ivar url: Camera's URL.
    :ivar executor: Executor of the camera.
    :ivar filters: Filters of the camera.
    """

    def __init__(self):
        self.id = None
        self.url = None
        self.executor = None
        self.filters = {}

    def add_filter(self, filter):
        """
        Set camera's filter.

        :param filter: Camera's filter.
        """
        id = filter.id
        if id in self.filters:
            raise ValueError("Filter with this ID already exists.")

        self.filters[id] = filter

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
