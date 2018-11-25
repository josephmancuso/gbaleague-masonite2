''' A Module Description '''
import pendulum
import requests

from app.Discord import Discord
from app.integrations.IntegrationDiscordDriver import IntegrationDiscordDriver
from app.League import League
from masonite.request import Request


class AppIntegrationsController:
    ''' Class Docstring Description '''

    def __init__(self, request: Request):
        self.request = request

    def show(self):
        league = League.find(self.request.param('id'))

        return view('leagues/apps', {'league': league})

    # def slack_send(self, IntegrationManager):
    #     print(IntegrationManager)
    #     return IntegrationManager.driver('slack').scopes('incoming-webhook').state(self.request.param('id')).redirect()

    # def slack_return(self, IntegrationManager):
    #     user = IntegrationManager.driver('slack').user()
    #     league = League.find(self.request.input('state'))

    #     webhook = user['incoming_webhook']['url']
    #     # print(webhook)
    #     requests.post(webhook, json={'text': 'Integrated With Masonite'})
    #     #channel
    #     channel = user['incoming_webhook']['channel']

    #     league.slackwebhook = webhook
    #     league.slackchannel = channel
    #     league.save()

    #     return self.request.redirect('http://localhost:8000/league/{0}/apps'.format(league.id))

    def send(self):
        league = League.find(self.request.param('league'))
        return IntegrationDiscordDriver().send(self.request, state=league.id, scopes=('webhook.incoming',))

    def get(self):
        response = IntegrationDiscordDriver().user(self.request)

        league = League.find(self.request.input('state'))
        discord = Discord.where('league_id', league.id).first()

        if not discord:
            Discord.create(
                access_token=response['access_token'],
                refresh_token=response['refresh_token'],
                scopes=response['scope'],
                expires_at=pendulum.now().add(seconds=response['expires_in']).to_datetime_string(),
                league_id=self.request.input('state'),
                channel_id=response['webhook']['id'],
                token=response['webhook']['token']
            )
        else:
            discord.access_token = response['access_token']
            discord.refresh_token = response['refresh_token']
            discord.scopes = response['scope']
            discord.expires_at = pendulum.now().add(seconds=response['expires_in']).to_datetime_string()
            discord.channel_id = response['webhook']['id']
            discord.token = response['webhook']['token']
            discord.save()

        league = League.find(self.request.input('state'))
        league.broadcast('Successfully integrated Discord with GBALeague.com')

        return self.request.redirect('http://localhost:8000/league/{0}/apps'.format(self.request.input('state')))
