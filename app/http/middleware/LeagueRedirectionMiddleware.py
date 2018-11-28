""" Load User Middleware"""

from app.League import League
from masonite.request import Request

class LeagueRedirectionMiddleware:
    """ Middleware class which loads the current user into the request """

    def __init__(self, request: Request):
        """ Inject Any Dependencies From The Service Container """
        self.request = request

    def before(self):
        """ Run This Middleware Before The Route Executes """
        if self.request.param('id'):
            try:
                if not League.find(self.request.param('id')):
                    self.request.session.flash('warning', 'That league does not exist')
                    self.request.redirect_to('discover')
            except:
                self.request.session.flash(
                    'warning', 'That league no longer exists')
                self.request.redirect_to('discover')

    def after(self):
        """ Run This Middleware After The Route Executes """
        pass
