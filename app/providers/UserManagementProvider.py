''' A UserManagementProvider Service Provider '''
from masonite.provider import ServiceProvider
from app.http.helpers.links.UserManagementLink import UserManagementLink, SwapUserLink
from app.User import User

class UserManagementProvider(ServiceProvider):

    wsgi = False

    def register(self):
        self.app.bind('UserManagementLink', UserManagementLink)
        self.app.bind('SwapLink', SwapUserLink)

    def boot(self, Request):
        Request.extend(RealUser)

class RealUser:

    def real_user(self):
        if self.get_cookie('_real_token'):
            return User.where('remember_token', self.get_cookie('_real_token')).first()
        
        return None