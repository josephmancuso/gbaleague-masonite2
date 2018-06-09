''' A Module Description '''

from app.League import League
from app.Team import Team
from slugify import slugify

class LeagueController(object):
    ''' Class Docstring Description '''

    def show(self):
        league = League.find(request().param('id'))

        return view('leagues/index', {'league': league})

    def teams(self):
        league = League.find(request().param('id'))
        teams = Team.where('league_id', league.id).get()

        return view('leagues/teams', {'league': league, 'teams': teams})

    def create(self):
        return view('create/leagues')

    def store(self):
        league = League.create(
            name = request().input('league-name'),
            owner_id = auth().id,
            description = request().input('league-overview'),
            slug = slugify(request().input('league-name')),
            current_id = None,
            draftorder = None,
        )

        request().redirect('/league/{0}'.format(league.id))

    def join(self):
        league = League.find(request().param('id'))
        return view('leagues/join', {'league': league})

    def skip(self):
        League.find(request().param('id')).skip_user()
        
        return request().redirect('/league/@id/draft')
