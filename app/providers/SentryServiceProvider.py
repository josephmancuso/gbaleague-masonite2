''' A SentryServiceProvider Service Provider '''
from masonite.provider import ServiceProvider

from ..helpers.SentryExceptionHook import SentryExceptionHook

class SentryServiceProvider(ServiceProvider):

    def register(self):
        self.app.bind('SentryExceptionHook', SentryExceptionHook())

    def boot(self):
        pass
