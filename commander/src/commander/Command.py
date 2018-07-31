class Command:
    """
    Command base class.

    Attributes:
        process: subprocess object.
            OS process.
    """

    def __init__(self):
        self.process = None

    def execute(self):
        """
        Execute command.
        """
        pass

    def stop(self):
        """
        Stop command.
        """
        pass
