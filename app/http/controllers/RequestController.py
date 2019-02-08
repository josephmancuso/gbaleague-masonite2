''' A Module Description '''

from app.League import League
from app.notifications import NewMemberNotification
from app.Requests import Requests
from app.Team import Team
from notifications import Notify


class RequestController:
    ''' Class Docstring Description '''

    def show(self):
        league = League.find(request().param('id'))

        requests = Requests.where('league_id', league.id).get()

        return view('leagues/requests', {'league': league, 'league_requests': requests})

    def store(self, notify: Notify):
        league = League.find(request().input('league'))
        Requests.create(
            team_id=request().input('team'),
            league_id=request().input('league')
        )

        team = Team.find(request().input('team'))

        league.broadcast('{0} owned by {1} has requested to join your league'.format(
            team.name, team.owner.name))

        notify.mail(NewMemberNotification, to=league.owner.email)

        return request().redirect('/league/@id/join?message=Requests Successfully Submitted!', {'id': league.id})

    def handle(self):
        league = League.find(request().input('league_id'))

        if request().has('accept'):
            # update team league_id
            team = Team().find(request().input('team_id'))
            team.league_id = request().input('league_id')
            team.save()

            # delete the request
            Requests.find(request().input('request_id')).delete()

            league.broadcast(
                '{} has joined the league!'.format(team.owner.name))

            request().session.flash('success', 'Accepted request')
            return request().redirect('/league/@id/requests', {'id': league.id})
                

        elif request().has('decline'):
            # simply delete request
            Requests.find(request().input('request_id')).delete()
            request().session.flash('success', 'Declined request')
            return request().redirect('/league/@id/requests', {'id': league.id})
            

        return request().redirect('/league/@id/requests?message=Unable to process request', {'id': league.id})
