''' A AppEventProvider Service Provider '''
from masonite.provider import ServiceProvider
# from app.events.UserSubscribed import UserSubscribed

class AppEventProvider(ServiceProvider):

    wsgi = False

    def register(self):
        pass

    def boot(self):
        # Event.listen('user.subscribed', [UserSubscribed])
        pass
