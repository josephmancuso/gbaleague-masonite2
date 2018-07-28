''' User Model '''

from config.database import Model
from app.Team import Team
from app.DraftedPokemon import DraftedPokemon
from app.League import League
from app.Requests import Requests as LeagueRequest
from billing.models.Billable import Billable

class User(Model, Billable):
    ''' User Model '''

    __fillable__ = ['name', 'email', 'password']

    __auth__ = 'email'

    def team(self, league):
        return Team.where('owner_id', self.id).where('league_id', league.id).first()

    def queued_pokemon(self, league):
        ''' Get all queued pokemon ID '''
        if self.team(league):
            return DraftedPokemon.where('league_id', league.id).where('team_id', self.team(league).id).get().pluck('queue_id')
        return []

    def get_queued_pokemon(self, league):
        if self.team(league):
            return DraftedPokemon \
                .where('league_id', league.id) \
                .where('team_id', self.team(league).id) \
                .where_null('pokemon_id') \
                .where_not_null('queue_id') \
                .get()
        return []

    def get_team_pokemon(self, league):
        if self.team(league):
            return DraftedPokemon.where('league_id', league.id).where('team_id', self.team(league).id).where_not_null('pokemon_id').get()
        return []

    def get_joinable_teams(self):
        return Team.where('owner_id', self.id).where_null('league_id').get()
    
    def get_all_teams(self):
        return Team.where('owner_id', self.id).get()

    def get_all_leagues(self):
        league_id_collection = Team.where('owner_id', self.id).where_not_null('league_id').get().pluck('league_id')
        return League.where_in('id', league_id_collection).get()

    def has_pending_request(self, league):
        if LeagueRequest.where('league_id', league.id).where_in('team_id', self.get_all_teams().pluck('id')).count():
            return True

        return False

    def is_league_owner(self, league):
        return league.owner_id == self.id

    def in_league(self, league):
        return Team.where('league_id', league.id).where('owner_id', self.id).get().count()

    def can_create_leagues(self):
        if self.is_subscribed():
            return True

        if League.where('owner_id', self.id).count() > 3:
            return False

        return True

    def can_create_teams(self):
        if self.is_subscribed():
            return True

        if Team.where('owner_id', self.id).count() > 5:
            return False

        return True
