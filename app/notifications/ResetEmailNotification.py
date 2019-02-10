''' A ResetEmailNotification Notification '''

from notifications import Notifiable
from masonite import env

class ResetEmailNotification(Notifiable):

    def mail(self):
        self.subject('GBALeague Password Reset') \
            .view('email/request_password', {'user': self._user, 'site': env('SITE')})
