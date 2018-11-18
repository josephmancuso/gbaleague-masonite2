''' A User Model Service Provider '''
import os

from events import Event
from masonite.provider import ServiceProvider
from masonite.request import Request

from app.commands.ShareCommand import ShareCommand
from app.commands.BroadcastWorkCommand import BroadcastWorkCommand
from app.drivers.BroadcastLocalDriver import BroadcastLocalDriver
from app.events import UserSignedUp
from app.User import User
from config import application
from masonite.view import View


class UserModelProvider(ServiceProvider):
    ''' Binds the User model into the Service Container '''

    wsgi = False

    def register(self):
        ''' Registers The User Into The Service Container '''
        self.app.bind('ShareCommand', ShareCommand())
        self.app.bind('BroadcastWorkCommand', BroadcastWorkCommand())
        self.app.bind('BroadcastLocalDriver', BroadcastLocalDriver)

    def boot(self, view: View, event: Event):
        view.share({
            'show_if': self._show_if,
            'env': os.getenv,
            'DEBUG': application.DEBUG
        })
        event.subscribe(UserSignedUp)

    @staticmethod
    def _show_if(output, check1, check2=False):
        if check2:
            if check1 == check2:
                return output
        else:
            if check1:
                return output
        return ''
