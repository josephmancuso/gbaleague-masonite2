''' A Module Description '''
import hashlib

from masonite.request import Request
from config import application
from masonite.auth import Auth
from masonite.helpers import password as bcrypt_password

from app.User import User
from app.validators.RegisterValidator import RegisterValidator


class LoginController:
    ''' Login Form Controller '''

    def __init__(self, request: Request):
        self.request = request

    def show(self):
        ''' Show the login page '''
        return view('auth/login', {'app': application, 'Auth': Auth(self.request)})

    def store(self):
        validate = RegisterValidator(self.request).login()
        if not validate.check():
            self.request.session.flash('validation', validate.errors())
            return self.request.redirect_to('login')

        self.check_old_encryption(self.request)

        if Auth(self.request).login(self.request.input('username'), self.request.input('password')):
            return self.request.redirect_to('discover')
        else:
            self.request.session.flash('danger', 'Invalid username or password')
            return self.request.redirect_to('login')
        return 'check terminal'

    def logout(self):
        Auth(self.request).logout()
        return self.request.redirect('/login')

    def check_old_encryption(self, request):
        user = User.where('email', request.input('username')).where('password', hashlib.sha1(
            request.input('password').encode('utf-8')).hexdigest()).first()
        if user:
            # login successful
            user.password = bcrypt_password(request.input('password'))
            user.save()
