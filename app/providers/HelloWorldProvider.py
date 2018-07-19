''' A HelloWorldProvider Service Provider '''
from masonite.provider import ServiceProvider
from dashboard.Link import BaseLink, UserLink

class HelloWorldLink(BaseLink):
    display = 'Hello World'
    url = '/dashboard/helloworld'

class ProfileLink(UserLink):
    display = 'Profile'    
    url = '/dashboard/profile'


class HelloWorldProvider(ServiceProvider):

    def register(self):
        self.app.bind('HelloWorld', HelloWorldLink)
        self.app.bind('Profile', ProfileLink)

    def boot(self):
        pass
