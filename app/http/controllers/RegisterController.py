""" A Module Description """
import json

from masonite.request import Request
from masonite import Queue
from config import application
from masonite.auth import Auth
from masonite.helpers import password as bcrypt_password

from app.notifications import WelcomeNotification
# from app.validators import RegisterValidator
from config import auth
from app.jobs import WelcomeEmailJob
from masonite.validation import Validator
from app.User import User


class RegisterController:
    """ Class Docstring Description """

    def __init__(self, request: Request):
        self.request = request

    def show(self, auth: Auth):
        """ Show the registration page """
        return view('auth/register', {'app': application, 'Auth': auth, 'json': json})

    def store(self, auth: Auth, request: Request, queue: Queue, validator: Validator):
        """ Register a new user """

        errors = request.validate(
            validator.required(['username', 'email', 'password']),
            validator.length('username', min=3, max=20),
            validator.length('email', min=3),
            validator.isnt(
                validator.is_in('email', User.all().pluck('email'), messages = {
                    'email': 'That email already exists'
                }),
            )
        )

        print(errors)

        if errors:
            return self.request.redirect_to('register').with_errors(errors)

        # register the user
        password = bcrypt_password(self.request.input('password'))

        auth.register({
            'name': self.request.input('username'),
            'password': self.request.input('password'),
            'email': self.request.input('email'),
        })

        # login the user
        # redirect to the homepage
        if auth.login(self.request.input('email'), self.request.input('password')):
            queue.push(WelcomeEmailJob, args=[self.request.input('email')])
            return self.request.redirect('/home')

        return self.request.redirect('/register')
