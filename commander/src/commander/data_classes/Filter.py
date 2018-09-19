import rospy


class Filter:
    """
    Filter class.

    :ivar id: ID of the filter.
    :ivar executor: Executor of the filter.
    :ivar type: Type of the filter.
    """

    def __init__(self):
        self.id = None
        self.executor = None
        self.type = None

    def to_dict(self):
        """
        Camera object to dictionary.

        :return: Dictionary of the camera object.
        """
        return {
            "id": self.id,
            "type": self.type,
            "topics_list": rospy.get_published_topics(self.id)
        }
