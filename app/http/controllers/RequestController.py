''' A Module Description '''

from app.Request import Request
from app.League import League
from app.Team import Team

class RequestController(object):
    ''' Class Docstring Description '''

    def show(self):
        league = League.find(request().param('id'))

        requests = Request.where('league_id', league.id).get()

        return view('leagues/requests', {'league': league, 'league_requests': requests})

    def store(self):
        league = League.find(request().input('league'))
        Request.create(
            team_id=request().input('team'),
            league_id=request().input('league')
        )

        team = Team.find(request().input('team'))

        league.broadcast('{0} owned by {1} has requested to join your league'.format(team.name, team.owner.name))

        return request().redirect('/league/@id/join?message=Request Successfully Submitted!')

    def handle(self):
        league = League.find(request().input('league_id'))

        if request().has('accept'):
            ## update team league_id
            team = Team().find(request().input('team_id'))
            team.league_id = request().input('league_id')
            team.save()

            ## delete the request
            Request.find(request().input('request_id')).delete()

            request().redirect( '/league/@id/requests?message=Accepted request').send({'id': league.id})

        elif request().has('decline'):
            ## simply delete request
            Request.find(request().input('request_id')).delete()
            request().redirect('/league/@id/requests?message=Declined request').send({'id': league.id})
