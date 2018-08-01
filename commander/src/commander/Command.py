class Command:
    """
    Command base class.

    Attributes:
        process: subprocess object.
            OS process.
    """

    def __init__(self):
        self.process = None

    def execute(self, **kwargs):
        """
        Execute command.

        Args:
            kwargs: key-worded arguments.
        """
        pass

    def stop(self):
        """
        Stop command.
        """
        pass
