import os
import signal
import subprocess


class Process:
    """
    Process utils class which helps
    to create or terminate process.
    """

    @staticmethod
    def create(*args):
        """
        Create process with given arguments.

        Args:
            args: argument lists.
        Returns:
            subprocess object.
                OS process.
        """
        process = subprocess.Popen(args)
        return process

    @staticmethod
    def terminate(process):
        """
        Terminate process with its children.

        Args:
            process: subprocess object.
                OS process.
        """
        ps_command = subprocess.Popen(
            "ps -o pid --ppid %d --noheaders" % process.pid, shell=True, stdout=subprocess.PIPE)
        ps_comand_output = ps_command.stdout.read()
        retcode = ps_command.wait()
        assert retcode == 0, "ps command returned %d" % retcode
        for pid_string in ps_comand_output.split("\n")[:-1]:
            os.kill(int(pid_string), signal.SIGINT)
        process.terminate()
