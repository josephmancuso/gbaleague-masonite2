''' A Schedule Database Model '''
from config.database import Model
from orator.orm import belongs_to

class Schedule(Model):

    __fillable__ = ['league_id', 'team1_id', 'team2_id', 'winner_id', 'scheduled_for']

    @belongs_to('team1_id', 'id')
    def team1(self):
        from app.Team import Team
        return Team

    @belongs_to('team2_id', 'id')
    def team2(self):
        from app.Team import Team
        return Team

    @belongs_to('winner_id', 'id')
    def winner(self):
        from app.Team import Team
        return Team
