''' A WelcomeNotification Notification '''
from notifications import Notifiable
from app.notifications.components.NexmoComponent import NexmoComponent


class WelcomeNotification(Notifiable, NexmoComponent):

    def mail(self):
        return self.subject('Welcome to the GBA!') \
            .panel('GBALeague.com') \
            .heading('You have successfully joined GBALeague.com') \
            .line('We wish you luck on your journey to becoming a GBA League champion!') \
            .line('If you have any questions be sure to reach out to us on Twitter @gbaleague_com')

    def text(self):
        print('to text: ', self._to)
        return self.message('A New Member Joined Your League.') \
            .message('Sign back in to accept them!')
