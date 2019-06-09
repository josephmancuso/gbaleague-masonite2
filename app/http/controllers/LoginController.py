''' A Module Description '''
import hashlib

from masonite.request import Request
from config import application
from masonite.auth import Auth
from masonite.helpers import password as bcrypt_password

from app.User import User
# from app.validators.RegisterValidator import RegisterValidator
from masonite.validation import Validator


class LoginController:
    ''' Login Form Controller '''

    def __init__(self, request: Request):
        self.request = request

    def show(self, auth: Auth):
        ''' Show the login page '''
        return view('auth/login', {'app': application, 'Auth': auth})

    def store(self, auth: Auth, validator: Validator):
        errors = self.request.validate(
            validator.required(['username', 'password']),
            validator.length(['username', 'password'], min=1, max=35),
            validator.is_in('username', User.all().pluck('email').map(lambda item: item.lower()), messages = {
                'username': 'Username or password is incorrect'
            })
        )

        if errors:
            return self.request.redirect_to('login').with_errors(errors)

        self.check_old_encryption(self.request)

        if auth.login(self.request.input('username'), self.request.input('password')):
            return self.request.redirect_to('discover')
        else:
            self.request.session.flash('danger', 'Invalid username or password')
            return self.request.redirect_to('login')

    def logout(self, auth: Auth):
        auth.logout()
        return self.request.redirect('/login')

    def check_old_encryption(self, request):
        user = User.where('email', request.input('username')).where('password', hashlib.sha1(
            request.input('password').encode('utf-8')).hexdigest()).first()
        if user:
            # login successful
            user.password = bcrypt_password(request.input('password'))
            user.save()
