class Executor:
    """
    Executor base class.

    :ivar process: subprocess object.
    """

    def __init__(self):
        self.process = None

    def execute(self, **kwargs):
        """
        Execute the executor.

        :param kwargs: key-worded arguments.
        """
        pass

    def stop(self):
        """
        Stop the executor.
        """
        pass

    def is_running(self, **kwargs):
        """
        Check if executor is running.

        :return: True if it's running, False if not.
        """
        pass
