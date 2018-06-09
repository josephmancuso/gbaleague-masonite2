''' A DraftedPokemon Database Model '''
from config.database import Model
from orator.orm import belongs_to

class DraftedPokemon(Model):
    __table__ = 'draftedpokemon'

    __fillable__ = ['team_id', 'pokemon_id', 'queue_id', 'league_id']

    @belongs_to('pokemon_id', 'id')
    def pokemon(self):
        from app.Pokemon import Pokemon
        return Pokemon

    @belongs_to('queue_id', 'id')
    def queued(self):
        from app.Pokemon import Pokemon
        return Pokemon
