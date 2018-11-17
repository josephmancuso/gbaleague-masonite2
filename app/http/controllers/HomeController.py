''' A Module Description '''
from masonite.auth import Auth
from masonite.request import Request
from config import application

class HomeController:
    ''' Home Dashboard Controller '''

    def __init__(self, request: Request):
        self.request = request

    def show(self):
        if not Auth(self.request).user():
            self.request.redirect('/login')
        return view('auth/home', {'app': application, 'Auth': Auth(self.request)})
