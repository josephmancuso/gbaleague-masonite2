''' A Module Description '''
from masonite.facades.Auth import Auth
from masonite.request import Request

class HomeController:
    ''' Home Dashboard Controller '''

    def __init__(self, request: Request):
        self.request = request

    def show(self, Application):
        if not Auth(self.request).user():
            self.request.redirect('/login')
        return view('auth/home', {'app': Application, 'Auth': Auth(self.request)})
