class Command:
    """
    Command base class.

    :ivar process: subprocess object.
    """

    def __init__(self):
        self.process = None

    def execute(self, **kwargs):
        """
        Execute the command.

        :param kwargs: key-worded arguments.
        """
        pass

    def stop(self):
        """
        Stop command.
        """
        pass
