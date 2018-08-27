''' A Module Description '''
import hashlib

from masonite.facades.Auth import Auth
from masonite.helpers import password as bcrypt_password

from app.User import User
from app.validators.RegisterValidator import RegisterValidator


class LoginController:
    ''' Login Form Controller '''

    def show(self, Request, Application):
        ''' Show the login page '''
        return view('auth/login', {'app': Application, 'Auth': Auth(Request)})

    def store(self, Request):
        validate = RegisterValidator(Request).login()
        if not validate.check():
            Request.session.flash('validation', validate.errors())
            return Request.redirect_to('login')

        self.check_old_encryption(Request)

        if Auth(Request).login(Request.input('username'), Request.input('password')):
            Request.redirect_to('discover')
        else:
            Request.session.flash('danger', 'Invalid username or password')
            Request.redirect_to('login')
        return 'check terminal'

    def logout(self, Request):
        Auth(Request).logout()
        return Request.redirect('/login')

    def check_old_encryption(self, request):
        user = User.where('email', request.input('username')).where('password', hashlib.sha1(
            request.input('password').encode('utf-8')).hexdigest()).first()
        if user:
            # login successful
            user.password = bcrypt_password(request.input('password'))
            user.save()
