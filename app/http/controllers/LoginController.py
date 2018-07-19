''' A Module Description '''
from masonite.facades.Auth import Auth

class LoginController:
    ''' Login Form Controller '''

    def show(self, Request, Application):
        ''' Show the login page '''
        Request.session.flash('back', 'redirection url')
        return view('auth/login', {'app': Application, 'Auth': Auth(Request)})

    def store(self, Request):
        print('store method', Request.session.get('back'))
        if Auth(Request).login(Request.input('username'), Request.input('password')):
            Request.redirect('/home')
        else:
            Request.redirect('/login')
        return 'check terminal'

    def logout(self, Request):
        Auth(Request).logout()
        return Request.redirect('/login')
