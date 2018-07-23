''' A Module Description '''
from app.User import User
import uuid
import os
from masonite.helpers import password as bcrypt_password

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


    def send(self, Mail):
        """ send reminder email """
        user = User.where('email', request().input('email')).first()
        if user:
            user.remember_token = str(uuid.uuid4())
            user.save()

            Mail.subject('GBALeague Password Reset').to(request().input('email')).template('email/request_password', {'user': user, 'site': os.getenv('SITE')}).send()
            request().session.flash('success', 'Email sent. Follow the instruction in the email to reset your password.')
        else:
            request().session.flash('error', 'No user found with that email address.')
            
        return request().back()
