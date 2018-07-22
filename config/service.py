import os

DRIVER = 'slack'

DRIVERS = {
    'slack': {
        'client': '140404785458.236564549872',
        'secret': '8fbb7888bf021a27394abc0eb5c78b36',
        'redirect': 'http://90bebe00.ngrok.io/oauth/slack'
    },
    'discord': {
        'client': os.getenv('DISCORD_CLIENT'),
        'secret': os.getenv('DISCORD_SECRET'),
        'redirect': os.getenv('DISCORD_REDIRECT'),
    }
}
