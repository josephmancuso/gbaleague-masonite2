''' A Discord Database Model '''
from config.database import Model

class Discord(Model):
    __table__ = 'discord'
    __fillable__ = ['access_token', 'refresh_token', 'scopes', 'league_id', 'expires_at', 'channel_id', 'token']
