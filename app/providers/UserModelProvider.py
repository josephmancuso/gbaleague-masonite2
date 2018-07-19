''' A User Model Service Provider '''
from masonite.provider import ServiceProvider
from app.User import User
from masonite.request import Request

class UserModelProvider(ServiceProvider):
    ''' Binds the User model into the Service Container '''

    wsgi = False

    def register(self):
        ''' Registers The User Into The Service Container '''
        self.app.bind('User', User)

    def boot(self):
        pass

class UserSubscribed:

    def handle(self):
        pass

