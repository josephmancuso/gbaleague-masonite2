''' A Module Description '''
from app.League import League
import requests

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

    def discord_send(self, IntegrationManager):
        return IntegrationManager.driver('discord').scopes('webhook.incoming').state(request().param('id')).redirect()

    def discord_return(self, IntegrationManager):
        response = IntegrationManager.driver('discord').user()

        channel_id = response['webhook']['channel_id']
        token = response['webhook']['token']
        d_id = response['webhook']['id']

        league = League.find(request().input('state'))

        league.discordid = d_id
        league.discordtoken = token
        league.discordchannel = channel_id
        league.save()

        league.broadcast('Successfully integrated Discord with GBALeague.com')
        return request().redirect('http://localhost:8000/league/{0}/apps'.format(league.id))

