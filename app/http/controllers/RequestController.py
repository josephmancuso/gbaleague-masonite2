''' A Module Description '''

from app.Requests import Requests
from app.League import League
from app.Team import Team

class RequestController(object):
    ''' Class Docstring Description '''

    def show(self):
        league = League.find(request().param('id'))

        requests = Requests.where('league_id', league.id).get()

        return view('leagues/requests', {'league': league, 'league_requests': requests})

    def store(self):
        league = League.find(request().input('league'))
        Requests.create(
            team_id=request().input('team'),
            league_id=request().input('league')
        )

        team = Team.find(request().input('team'))

        league.broadcast('{0} owned by {1} has requested to join your league'.format(team.name, team.owner.name))

        return request().redirect('/league/@id/join?message=Requests Successfully Submitted!', {'id': league.id})

    def handle(self):
        league = League.find(request().input('league_id'))

        if request().has('accept'):
            ## update team league_id
            team = Team().find(request().input('team_id'))
            team.league_id = request().input('league_id')
            team.save()

            ## delete the request
            Requests.find(request().input('request_id')).delete()

            return request() \
                .redirect( '/league/@id/requests', {'id': league.id}) \
                .session.flash('success' 'Accepted request')

        elif request().has('decline'):
            ## simply delete request
            Requests.find(request().input('request_id')).delete()
            return request() \
                .redirect('/league/@id/requests', {'id': league.id}) \
                .session.flash('success', 'Declined request')
        
        return request().redirect('/league/@id/requests?message=Unable to process request', {'id': league.id})
