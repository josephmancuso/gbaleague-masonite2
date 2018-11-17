''' A Module Description '''

from app.Team import Team


class TeamController:
    ''' Class Docstring Description '''

    def show(self):
        if request().has('back'):
            request().session.flash('back', request().input('back'))
        
        print('viewing??')
        return view('create/team')

    def store(self, Upload):
        try:
            logo = request().input('logo').filename
        except AttributeError:
            logo = ''

        create_team = Team.create(
            name=request().input('name'),
            owner_id=auth().id,
            picture=logo
        )

        # upload logo
        if logo:
            Upload.store(request().input('logo'))

        if create_team:
            return request().back(default='create/team?message=Created Successfully')

        return request().redirect('/create/team?message=Could Not Create Team')
