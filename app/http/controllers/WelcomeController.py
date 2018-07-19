""" Welcome The User To Masonite """
from masonite.request import Request
from masonite.view import View

from app.League import League


class WelcomeController:
    """ Controller For Welcoming The User """

    def __init__(self, view: View, request: Request):
        self.view = view
        self.request = request

    def show(self) -> View.render:
        ''' Show Welcome Template '''

        return self.view.render('index')

    def discover(self) -> View.render:
        """Shows the discover page

        Returns:
            View.render
        """

        if self.request.input('search'):
            leagues = League.all().filter(lambda league: self.request.input(
                'search').lower() in league.name.lower())
        else:
            leagues = League.all()

        return self.view.render('discover', {'leagues': leagues})

    def slack(self):
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
