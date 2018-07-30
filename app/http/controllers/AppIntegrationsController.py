''' A Module Description '''
import pendulum
import requests

from app.Discord import Discord
from app.integrations.IntegrationDiscordDriver import IntegrationDiscordDriver
from app.League import League


class AppIntegrationsController:
    ''' Class Docstring Description '''

    def show(self):
        league = League.find(request().param('id'))

        return view('leagues/apps', {'league': league})

    def slack_send(self, IntegrationManager):
        return IntegrationManager.driver('slack').scopes('incoming-webhook').state(request().param('id')).redirect()

    def slack_return(self, IntegrationManager):
        user = IntegrationManager.driver('slack').user()
        league = League.find(request().input('state'))

        webhook = user['incoming_webhook']['url']
        # print(webhook)
        requests.post(webhook, json={'text': 'Integrated With Masonite'})
        #channel
        channel = user['incoming_webhook']['channel']

        league.slackwebhook = webhook
        league.slackchannel = channel
        league.save()

        return request().redirect('http://localhost:8000/league/{0}/apps'.format(league.id))

    def send(self, Request):
        league = League.find(Request.param('league'))
        return IntegrationDiscordDriver().send(Request, state=league.id, scopes=('webhook.incoming',))

    def get(self, Request):
        response = IntegrationDiscordDriver().user(Request)

        league = League.find(Request.input('state'))
        discord = Discord.where('league_id', league.id).first()

        if not discord:
            Discord.create(
                access_token= response['access_token'],
                refresh_token = response['refresh_token'],
                scopes = response['scope'],
                expires_at = pendulum.now().add(seconds=response['expires_in']).to_datetime_string(),
                league_id=Request.input('state'),
                channel_id = response['webhook']['id'],
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

        league = League.find(Request.input('state'))
        league.broadcast('Successfully integrated Discord with GBALeague.com')

        return request().redirect('http://localhost:8000/league/{0}/apps'.format(Request.input('state')))
