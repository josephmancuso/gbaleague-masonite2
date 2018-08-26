""" A ShareCommand Command """
from cleo import Command
import subprocess


class ShareCommand(Command):
    """
    Description of command

    share
    """

    def handle(self):
        subprocess.Popen(['~/ngrok http 5000'], shell=True)
        subprocess.call(['craft serve --port 5000'], shell=True)
