''' A User Model Service Provider '''
from masonite.provider import ServiceProvider
from app.User import User
from masonite.request import Request

class UserModelProvider(ServiceProvider):
    ''' Binds the User model into the Service Container '''

    wsgi = False

    def register(self):
        ''' Registers The User Into The Service Container '''
        pass

    def boot(self, ViewClass):
        ViewClass.share({
            'show_if': self._show_if
        })
    
    @staticmethod
    def _show_if(output, check1, check2=False):
        print(check1)
        if check2:
            if check1 == check2:
                return output
        else:
            if check1:
                return output
        return ''
