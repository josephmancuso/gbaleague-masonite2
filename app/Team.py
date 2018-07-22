''' A Team Database Model '''
from config.database import Model
from orator.orm import belongs_to

from app.DraftedPokemon import DraftedPokemon

class Team(Model):
    __fillable__ = ['name', 'league_id', 'owner_id', 'picture']

    def get_team_pokemon(self, league=False):
        if league:
            return DraftedPokemon \
                .where('team_id', self.id) \
                .where('league_id', league.id) \
                .where_not_null('pokemon_id') \
                .get()
        else:
            return DraftedPokemon \
                .where('team_id', self.id) \
                .where('league_id', self.league_id) \
                .where_not_null('pokemon_id') \
                .get()
    
    @belongs_to('owner_id', 'id')
    def owner(self):
        from app.User import User
        return User
