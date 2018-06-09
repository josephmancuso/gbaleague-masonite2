''' Welcome The User To Masonite '''
import requests

from app.League import League
from app.User import User

class WelcomeController:
    ''' Controller For Welcoming The User '''

    def show(self, Cache):
        ''' Show Welcome Template '''
        # return request().redirect('/login')
        # self.cache.store('key', 'new value bitches')
        return view('index')

    def discover(self, Session):
        # self.cache.store('key', 'new value bitches')
        if request().input('search'):
            leagues = League.all().filter(lambda league: request().input('search').lower() in league.name.lower())
        else:
            leagues = League.all()

        return view('discover', {'leagues': leagues})

    def slack(self, IntegrationManager):
        return ''
        # response = IntegrationManager.driver('discord').user()

        # requests.post(
        #     'https://discordapp.com/api/webhooks/{0}/{1}'.format(
        #         response['webhook']['id'],
        #         response['webhook']['token']
        #     ),
        #     json={
        #         'content': 'Masonite was successfully integrated!',
        #         'username': 'Masonite'
        #     }
        # )
        # return response['access_token']
