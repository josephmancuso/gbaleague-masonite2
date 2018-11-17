""" League Owner Middleware """
from app.League import League
from masonite.request import Request

class LeagueOwner:
    """ Middleware to check if the user is the owner of the league """

    def __init__(self, request: Request):
        """ Inject Any Dependencies From The Service Container """
        self.request = request

    def before(self):
        """ Run This Middleware Before The Route Executes """

        if self.request.user():
            if not League.where('owner_id', self.request.user().id).where('id', self.request.param('id')).first():
                raise Exception('You are not the league owner.')

    def after(self):
        """ Run This Middleware After The Route Executes """
        pass
