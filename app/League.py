''' A League Database Model '''
import requests
from backpack import collect
from orator.orm import belongs_to, has_many

from app.Schedule import Schedule
from app.Team import Team
from app.Discord import Discord

from config import database
from config.database import Model


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

    def is_drafting(self):
        return self.status == 1

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

    def has_member_limit(self):
        if self.owner.is_subscribed():
            return False

        if self.get_teams().count() >= 6:
            return True

    def get_schedule(self):
        return Schedule.where('league_id', self.id).get()

    def get_teams(self):
        return Team.where('league_id', self.id).get()

    def start_draft(self):
        self.draftorder = ''
        for team in self.get_teams():
            self.draftorder += str(team.owner_id) + ','

        self.draftorder = self.draftorder[:-1]
        if not self.current_id:
            self.current_id = self.draftorder.split(',')[0]

        self.status = 1
        self.save()

    def close_draft(self):
        self.status = 0
        self.save()

    def broadcast(self, message):
        channels = Discord.where('league_id', self.id).get()
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        for channel in channels:
            requests.post('https://discordapp.com/api/webhooks/{}/{}'.format(channel.channel_id, channel.token), data={'content': message, 'username': 'GBALeague.com'}, headers=headers)

    def get_discord(self):
        return Discord.where('league_id', self.id).first()

    def has_discord(self):
        if self.get_discord():
            return True
        return False
