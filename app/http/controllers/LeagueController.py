''' A Module Description '''
from masonite.view import View
from masonite.request import Request
from app.League import League
from app.Team import Team
from slugify import slugify

class LeagueController:
    ''' Class Docstring Description '''

    def __init__(self, league: League, view: View, request: Request):
        self.league = league
        self.view = view
        self.request = request

    def show(self):
        league = self.league.find(request().param('id'))

        return view('leagues/index', {'league': league})

    def teams(self):
        league = League.find(request().param('id'))
        teams = Team.where('league_id', league.id).get()

        return view('leagues/teams', {'league': league, 'teams': teams})

    def create(self):
        return view('create/leagues')

    def store(self):
        print('storing')
        league = League.create(
            name = request().input('league-name'),
            owner_id = auth().id,
            description = request().input('league-overview'),
            slug = slugify(request().input('league-name')),
            current_id = None,
            draftorder = None,
        )

        print('storing')

        request().redirect('/league/{0}'.format(league.id))

    def join(self):
        league = League.find(request().param('id'))
        return view('leagues/join', {'league': league})

    def skip(self):
        league = League.find(request().param('id'))
        league.skip_user()

        request().session.flash('info', 'User Skipped!')

        return request().redirect_to('league.draft', {'id': league.id})

    def delete(self):
        League.find(request().param('id')).delete()

        return request().redirect_to('discover')

    def edit(self):
        league = League.find(request().param('id'))
        return self.view.render('leagues/edit', {'league': league})

    def store_edit(self):
        league = League.find(request().param('id'))
        league.description = self.request.input('overview')
        league.save()

        return self.request.redirect_to('league.id', {'id': league.id})
