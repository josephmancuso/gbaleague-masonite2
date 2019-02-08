''' A WelcomeEmailJob Queue Job '''

from masonite.queues import Queueable
from app.notifications import WelcomeNotification
from notifications import Notify
 
class WelcomeEmailJob(Queueable):

    def __init__(self, notify: Notify):
        self.notify = notify

    def handle(self, email):
        self.notify.mail(WelcomeNotification, to=email)

