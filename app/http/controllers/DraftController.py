''' A Module Description '''

from app.DraftedPokemon import DraftedPokemon
from masonite.request import Request
from app.League import League
from app.Pokemon import Pokemon
from app.Team import Team


class DraftController:
    ''' Class Docstring Description '''

    def __init__(self, request: Request):
        self.request = request
        self.league = League.find(request.param('id'))
        pass

    def show(self):
        if self.request.has('tier'):
            tier = self.request.input('tier')
        else:
            tier = 1

        return view('leagues/draft', {'league': self.league, 'tier': tier})

    def draft(self, Request):
        if self.request.has('draft'):
            DraftedPokemon.create(
                team_id=self.league.current.team(self.league).id,
                pokemon_id=self.request.input('pokemon'),
                league_id=self.league.id
            )

            DraftedPokemon.where('queue_id', self.request.input(
                'pokemon')).where('league_id', self.league.id).delete()

            # Get Pokemon
            pokemon = Pokemon.find(self.request.input('pokemon'))
            team = Team.find(self.league.current.team(self.league).id)

            team.points -= pokemon.points
            team.save()

            self.league.broadcast('{} was drafted by {} for {} points'.format(pokemon.name, team.name, pokemon.points))

            self.league.next_drafter()

            self.league.broadcast("It is currently {}'s turn to draft.".format(team.owner.name))

            self.request.redirect_to('league.draft', {'id': self.league.id}) \
                .session.flash('success', 'Successfully Drafted {0}'.format(pokemon.name))

        elif self.request.has('unqueue'):
            DraftedPokemon \
                .where('queue_id', self.request.input('pokemon')) \
                .where('team_id', self.request.user()
                       .team(self.league).id).where('league_id', self.league.id) \
                .first().delete()

            return self.request.redirect_to('league.draft', {'id': self.league.id}) \
                .session.flash('success', 'Successfully Unqueued')

        elif self.request.has('queue'):
            DraftedPokemon.create(
                team_id=auth().team(self.league).id,
                queue_id=self.request.input('pokemon'),
                league_id=self.league.id
            )
            return self.request.redirect_to('league.draft', {'id': self.league.id}) \
                .session.flash('success', 'Queue Successful')
        
        self.request.session.flash('warning', 'Could not draft at this time')
        return self.request.redirect_to('league.draft', {'id': self.league.id})

    def status(self):
        league = League.find(request().param('id'))
        if request().has('draft-open'):
            league.start_draft()
            league.broadcast('The draft has started!')
        elif request().has('draft-close'):
            league.close_draft()
            league.broadcast('The draft is closed!')

        return request().redirect('/league/{0}/draft'.format(league.id))
