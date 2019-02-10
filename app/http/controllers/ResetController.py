''' A Module Description '''
import os
import uuid

from masonite import Mail, Queue
from masonite.helpers import password as bcrypt_password

from app.jobs import ResetEmail
from app.User import User


class ResetController:
    ''' Class Docstring Description '''

    def forgot(self):
        return view('auth/forgot')

    def reset(self):
        if not request().has('v'):
            raise Exception

        user = User.where('remember_token', request().input('v')).first()
        if user:
            return view('auth/reset')

    def password(self):
        user = User.where('remember_token', request().input('v')).first()
        if user:
            user.password = bcrypt_password(request().input('password'))
            user.save()
            return request().redirect_to('login')

    def send(self, mail: Mail, queue: Queue):
        """ send reminder email """
        user = User.where('email', request().input('email')).first()
        if user:
            if not user.remember_token:
                user.remember_token = str(uuid.uuid4())
                user.save()
            
            queue.push(ResetEmail, args=(user,))

            request().session.flash('success',
                                    'Email sent. Follow the instruction in the email to reset your password.')
        else:
            request().session.flash('error', 'No user found with that email address.')

        return request().back()
