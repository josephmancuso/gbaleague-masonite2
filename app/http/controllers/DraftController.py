''' A Module Description '''

from app.League import League
from app.DraftedPokemon import DraftedPokemon
from app.Pokemon import Pokemon
from app.Team import Team

class DraftController(object):
    ''' Class Docstring Description '''

    def show(self, Request):
        league = League.find(Request.param('id'))

        if request().has('tier'):
            tier = request().input('tier')
        else:
            tier = 1

        return view('leagues/draft', {'league': league, 'tier': tier})

    def draft(self, Request):
        league = League.find(Request.param('id'))

        if Request.has('draft'):
            DraftedPokemon.create(
                team_id=league.current.team(league).id,
                pokemon_id=Request.input('pokemon'),
                league_id=league.id
            )

            DraftedPokemon.where('queue_id', Request.input(
                'pokemon')).where('league_id', league.id).delete()

            # Get Pokemon
            pokemon = Pokemon.find(Request.input('pokemon'))
            team = Team.find(league.current.team(league).id)

            league.broadcast('{0} was drafted by {1}'.format(pokemon.name, team.name))

            league.next_drafter()

            return Request.redirect('/league/@id/draft') \
                .session.flash('success', 'Successfully Drafted {0}'.format(pokemon.name))

        elif Request.has('unqueue'):
            DraftedPokemon \
                .where('queue_id', Request.input('pokemon')) \
                .where('team_id', Request.user()
                       .team(league).id).where('league_id', league.id) \
                .first().delete()

            return Request.redirect('/league/@id/draft') \
                .session.flash('success', 'Successfully Unqueued')

        elif Request.has('queue'):
            DraftedPokemon.create(
                team_id=auth().team(league).id,
                queue_id=Request.input('pokemon'),
                league_id=league.id
            )
            return Request.redirect('/league/@id/draft') \
                .session.flash('success', 'Queue Successful')

        return Request.redirect('/league/@id/draft?message=Could not draft at this time')

    def status(self):
        league = League.find(request().param('id'))
        if request().has('draft-open'):
            league.status = 1
        elif request().has('draft-close'):
            league.status = 0
        
        league.save()

        return request().redirect('/league/{0}/draft'.format(league.id))

    