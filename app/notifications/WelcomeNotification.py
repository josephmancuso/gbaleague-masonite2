''' A WelcomeNotification Notification '''
from notifications import Notifiable

class WelcomeNotification(Notifiable):

    def mail(self):
        return self.subject('Welcome to the GBA!') \
            .panel('GBALeague.com') \
            .heading('You have successfully joined GBALeague.com') \
            .line('We wish you luck on your journey to becoming a GBA League champion!') \
            .line('If you have any questions be sure to reach out to us on Twitter @gbaleague_com')
