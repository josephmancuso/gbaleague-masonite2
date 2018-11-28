''' A SentryServiceProvider Service Provider '''
from masonite.provider import ServiceProvider

from app.helpers.SentryExceptionHook import SentryExceptionHook
from config import application


class SentryServiceProvider(ServiceProvider):

    wsgi = False

    def register(self):
        if not application.DEBUG:
            self.app.bind('SentryExceptionHook', SentryExceptionHook())

    def boot(self):
        pass
