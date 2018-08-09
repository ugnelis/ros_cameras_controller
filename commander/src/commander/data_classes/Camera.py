class Camera:
    """
    Camera class.

    :ivar id: Camera's id.
    """

    def __init__(self):
        self.id = None
        self.topics_list = []

    def set_id(self, id):
        """
        Set camera's id.

        :param id: Camera's id.
        """
        self.id = id

    def set_topics_list(self, topics_list):
        """
        Set camera's list of the topics.

        :param topics_list: camera's list of the topics.
        """
        self.topics_list = topics_list

    def to_dict(self):
        """
        Camera object to dictionary.

        :return: Dictionary of the camera object.
        """
        return {
            "id": self.id,
            "topics_list": self.topics_list
        }
