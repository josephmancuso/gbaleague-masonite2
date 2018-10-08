''' A WelcomeEmailJob Queue Job '''

from masonite.queues import Queueable
from app.notifications import WelcomeNotification

class WelcomeEmailJob(Queueable):

    def __init__(self, Notify):
        self.notify = Notify

    def handle(self, email):
        self.notify.mail(WelcomeNotification, to=email)

