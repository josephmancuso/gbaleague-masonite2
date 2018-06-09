''' A League Database Model '''
from config.database import Model
from config import database
from orator.orm import belongs_to, has_many
from backpack import collect

from app.Schedule import Schedule
from app.Team import Team
import requests

class League(Model):

    __fillable__ = ['name', 'owner_id', 'description', 'slug', 'current_id', 'draftorder']

    @belongs_to('current_id', 'id')
    def current(self):
        from app.User import User
        return User

    @belongs_to('owner_id', 'id')
    def owner(self):
        from app.User import User
        return User

    def draft_status(self):
        if self.status == 0:
            return 'Closed'
        elif self.status == 1:
            return 'Open'

        return 'Unknown'

    def draftable_pokemon(self, tier=None):
        id_collection = database.DB.table('draftedpokemon').where_not_null('pokemon_id').get().pluck('pokemon_id')
        pokemon = database.DB.table(
            'pokemon').where_not_in('id', id_collection).order_by('name', 'asc')

        if tier:
            pokemon.where('tier', str(tier))

        return pokemon.get()

    def next_drafter(self):
        # ordering 0 -->
        # ordering 1 <--
        # change the drafter to the next drafter

        current_drafter = self.current_id
        draft_order = collect(self.draftorder.split(','))
        next_drafter = None
        i = 0

        for drafter in draft_order:
            if self.ordering == 0:
                if drafter == str(current_drafter):
                    try:
                        next_drafter = draft_order[i+1]
                        break
                    except IndexError:
                        next_drafter = draft_order[i]
                        self.ordering = 1
                        break
            else:
                if drafter == str(current_drafter):
                    if drafter == draft_order[0]:
                        # user if the first one
                        next_drafter = draft_order[i]
                        self.ordering = 0
                    else:
                        next_drafter = draft_order[i-1]
            i += 1

        self.current_id = next_drafter
        self.save()

    def skip_user(self):
        current_drafter = self.current_id
        self.next_drafter()

        if int(self.current_id) == int(current_drafter):
            self.next_drafter()

    def get_schedule(self):
        return Schedule.where('league_id', self.id).get()

    def get_teams(self):
        return Team.where('league_id', self.id).get()

    def broadcast(self, message):
        if self.slackwebhook:
            requests.post(self.slackwebhook, json={'text': message})
        
        if self.discordid:
            requests.post('https://discordapp.com/api/webhooks/{0}/{1}'.format(self.discordid, self.discordtoken), json={'content': message, 'username': 'GBALeague.com'})

    @has_many
    def buff_breakers(self):
        from app.Team import Team
        return Team.order_by('id', 'name').distinct()
