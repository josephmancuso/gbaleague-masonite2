''' A SentryServiceProvider Service Provider '''
from masonite.provider import ServiceProvider

from ..helpers.SentryExceptionHook import SentryExceptionHook

class SentryServiceProvider(ServiceProvider):

    def register(self):
        if self.app.make('Application').DEBUG == 'False':
            self.app.bind('SentryExceptionHook', SentryExceptionHook())

    def boot(self):
        pass
