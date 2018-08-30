""" A UserSignedUp Event """
from events import Event
from app.notifications import WelcomeNotification

class UserSignedUp(Event):
    """ UserSignedUp Event Class """

    subscribe = [
        'user.signedup'
    ]

    def __init__(self, Notify):
        """ Event Class Constructor """
        self.notify = Notify

    def handle(self):
        """ Event Handle Method """
        self.notify.mail(WelcomeNotification, to='idmann509@gmail.com')
