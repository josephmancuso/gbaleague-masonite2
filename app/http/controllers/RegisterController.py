""" A Module Description """
from masonite.facades.Auth import Auth
from config import auth
import bcrypt
from masonite.helpers import password as bcrypt_password
from app.validators import RegisterValidator
import json
import hashlib


class RegisterController:
    """ Class Docstring Description """

    def __init__(self):
        pass

    def show(self, Request, Application):
        """ Show the registration page """
        return view('auth/register', {'app': Application, 'Auth': Auth(Request), 'json': json})

    def store(self, Request):
        """ Register a new user """

        validate = RegisterValidator(Request).register()
        print(Request.all())
        print(validate.check(), validate.errors())
        print('sha1:', hashlib.sha1(Request.input('password').encode('utf-8')).hexdigest())


        if not validate.check():
            Request.session.flash('validation', json.dumps(validate.errors()))
            return Request.redirect_to('register')

        return
        # register the user
        password = bcrypt_password(Request.input('password'))
        
        print('creating password:', password)

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
