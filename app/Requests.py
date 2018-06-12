''' A Request Database Model '''
from config.database import Model
from orator.orm import belongs_to

class Requests(Model):
    __fillable__ = ['team_id', 'league_id']
    __table__ = 'requests'

    @belongs_to('team_id', 'id')
    def team(self):
        from app.Team import Team
        return Team
