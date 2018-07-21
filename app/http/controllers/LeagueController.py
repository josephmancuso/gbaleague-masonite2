""" A Module Description """
from masonite.request import Request
from masonite.view import View
from slugify import slugify

from app.League import League
from app.Team import Team


class LeagueController:
    """ Class Docstring Description """

    def __init__(self, league: League, view: View, request: Request):
        self.view = view
        self.request = request
        self.league = league.find(self.request.param('id'))

    def show(self):
        league = self.league.find(self.request.param('id'))

        return self.view.render('leagues/index', {'league': league})

    def teams(self):
        teams = Team.where('league_id', self.league.id).get()

        return self.view.render('leagues/teams', {'league': self.league, 'teams': teams})

    def create(self):
        return self.view.render('create/leagues')

    def store(self):
        league = League.create(
            name=self.request.input('league-name'),
            owner_id=self.request.user().id,
            description=self.request.input('league-overview'),
            slug=slugify(self.request.input('league-name')),
            current_id=None,
            draftorder=None,
        )

        return self.request.redirect_to('league.id', {'id': league.id})

    def join(self):
        return self.view.render('leagues/join', {'league': self.league})

    def skip(self):
        self.league.skip_user()

        self.request.session.flash('info', 'User Skipped!')

        return self.request.redirect_to('league.draft', {'id': self.league.id})

    def delete(self):
        self.league.delete()

        return self.request.redirect_to('discover')

    def edit(self):
        return self.view.render('leagues/edit', {'league': self.league})

    def points(self):
        team = Team.find(self.request.input('team'))
        team.points = self.request.input('points')
        team.save()

        self.request.session.flash('success', 'Successfully Changed Points')
        return self.request.back()

    def remove(self):
        team = Team.find(self.request.input('team'))
        team.league_id = None
        team.save()

        self.request.session.flash('success', 'Successfully Removed Team')
        return self.request.back()

    def store_edit(self):
        self.league.description = self.request.input('overview')
        self.league.save()

        return self.request.redirect_to('league.id', {'id': self.league.id})
