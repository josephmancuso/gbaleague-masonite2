""" Load User Middleware"""

from app.League import League

class LeagueRedirectionMiddleware:
    """ Middleware class which loads the current user into the request """

    def __init__(self, Request):
        """ Inject Any Dependencies From The Service Container """
        self.request = Request

    def before(self):
        """ Run This Middleware Before The Route Executes """
        if self.request.param('id'):
            if not League.find(self.request.param('id')):
                self.request.session.flash('warning', 'That League does not exist')
                self.request.redirect_to('discover')

    def after(self):
        """ Run This Middleware After The Route Executes """
        pass
