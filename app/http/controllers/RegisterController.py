""" A Module Description """
import json

from masonite.facades.Auth import Auth
from masonite.helpers import password as bcrypt_password

from app.notifications import WelcomeNotification
from app.validators import RegisterValidator
from config import auth


class RegisterController:
    """ Class Docstring Description """

    def __init__(self):
        pass

    def show(self, Request, Application):
        """ Show the registration page """
        return view('auth/register', {'app': Application, 'Auth': Auth(Request), 'json': json})

    def store(self, Request, Notify):
        """ Register a new user """

        validate = RegisterValidator(Request).register()
        if validate.check():
            validate.check_exists()

        if not validate.check():
            Request.session.flash('validation', json.dumps(validate.errors()))
            return Request.redirect_to('register')

        # register the user
        password = bcrypt_password(Request.input('password'))

        auth.AUTH['model'].create(
            name=Request.input('username'),
            password=password,
            email=Request.input('email'),
        )

        # login the user
        # redirect to the homepage
        if Auth(Request).login(Request.input(auth.AUTH['model'].__auth__), Request.input('password')):
            return Request.redirect('/home')

        return Request.redirect('/register')
