from masonite import env

DRIVER = 'discord'

DRIVERS = {
    'discord': {
        'client': env('DISCORD_CLIENT'),
        'secret': env('DISCORD_SECRET'),
        'redirect': env('DISCORD_REDIRECT'),
    }
}
