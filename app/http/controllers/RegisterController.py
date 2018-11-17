""" A Module Description """
import json

from masonite.request import Request
from masonite import Queue
from config import application
from masonite.auth import Auth
from masonite.helpers import password as bcrypt_password

from app.notifications import WelcomeNotification
from app.validators import RegisterValidator
from config import auth
from app.jobs import WelcomeEmailJob


class RegisterController:
    """ Class Docstring Description """

    def __init__(self, request: Request):
        self.request = request

    def show(self):
        """ Show the registration page """
        return view('auth/register', {'app': application, 'Auth': Auth(self.request), 'json': json})

    def store(self, queue: Queue):
        """ Register a new user """

        validate = RegisterValidator(self.request).register()
        if validate.check():
            validate.check_exists()

        if not validate.check():
            self.request.session.flash('validation', json.dumps(validate.errors()))
            return self.request.redirect_to('register')

        # register the user
        password = bcrypt_password(self.request.input('password'))

        auth.AUTH['model'].create(
            name=self.request.input('username'),
            password=password,
            email=self.request.input('email'),
        )

        # login the user
        # redirect to the homepage
        if Auth(self.request).login(self.request.input(auth.AUTH['model'].__auth__), self.request.input('password')):
            queue.push(WelcomeEmailJob, args=[self.request.input('email')])
            return self.request.redirect('/home')

        return self.request.redirect('/register')
