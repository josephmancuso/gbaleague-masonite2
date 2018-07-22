import os

DRIVER = 'discord'

DRIVERS = {
    'discord': {
        'client': os.getenv('DISCORD_CLIENT'),
        'secret': os.getenv('DISCORD_SECRET'),
        'redirect': os.getenv('DISCORD_REDIRECT'),
    }
}
