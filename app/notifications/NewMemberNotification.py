''' A NewMemberNotification Notification '''
from notifications import Notifiable
import os

class NewMemberNotification(Notifiable):

    def mail(self):
        return self.subject('GBALeague.com New Member Request') \
            .panel('GBALeague.com') \
            .heading('A New Request!') \
            .line('A new member head requested to join your league! Sign back in to accept them') \
            .action('Sign In', href="{}{}".format(os.getenv('SITE'), '/login'))
