''' A Module Description '''

from app.Schedule import Schedule
from app.League import League
import datetime

class ScheduleController(object):
    ''' Class Docstring Description '''

    def show(self):
        league = League.find(request().param('id'))
        schedules = Schedule.where('league_id', league.id).get()
        return view('leagues/schedule', {'schedules': schedules, 'league': league})

    def store(self):
        league = League.find(request().input('league_id'))
        dt = datetime.datetime.strptime(request().input('scheduled_time'), '%m/%d/%Y')

        Schedule.create(
            league_id=league.id,
            team1_id=request().input('team1'),
            team2_id=request().input('team2'),
            scheduled_for=dt.strftime('%Y-%m-%d'),
        )

        return request().redirect('/league/{0}/schedule'.format(league.id))

    def delete(self):
        Schedule.find(request().input('schedule_id')).delete()

        return request().redirect("/league/{0}/schedule?message=Schedule Removed".format(request().param('id')))
