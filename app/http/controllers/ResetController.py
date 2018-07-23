''' A Module Description '''
from app.User import User
import uuid
import os

class ResetController:
    ''' Class Docstring Description '''

    def forgot(self):
        print('inside forgot')
        return view('auth/forgot')

    def reset(self):
        user = User.where('remember_token', request().input('v')).first()
        if user:
            return view('auth/reset')


    def send(self, Mail):
        """ send reminder email """
        print('send mail')
        user = User.where('email', request().input('email')).first()
        if user:
            user.remember_token = str(uuid.uuid4())
            user.save()
            print('sending mail')

            Mail.subject('GBALeague Password Reset').to(request().input('email')).template('email/request_password', {'user': user, 'site': os.getenv('SITE')}).send()

        return 'message sent'
