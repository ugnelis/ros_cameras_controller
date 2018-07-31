class Command:
    """
    Command base class.

    Attributes:
        process: subprocess object.
            OS process.
    """

    def __init__(self):
        self.process = None

    def execute(self, argument):
        """
        Execute command.

        Args:
            argument: argument.
        """
        pass

    def stop(self):
        """
        Stop command.
        """
        pass
