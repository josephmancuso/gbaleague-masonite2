""" A ResetEmail Queue Job """

from masonite.queues import Queueable
from notifications import Notify
from app.notifications import ResetEmailNotification

class ResetEmail(Queueable):
    """A ResetEmail Job
    """

    def __init__(self, notify: Notify):
        """A ResetEmail Constructor
        """

        self.notify = notify

    def handle(self, user):
        """Logic to handle the job
        """

        return self.notify.mail(ResetEmailNotification, user=user, to=user.email)
