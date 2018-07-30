""" A Module Description """

from masonite.view import View


class SettingsController:
    """ Class Docstring Description """

    def __init__(self, view: View):
        self.view = view

    def show(self):
        """ Show the setting page """
        return self.view.render('settings/show')

    def leagues(self):
        return self.view.render('settings/leagues')

    def teams(self):
        return self.view.render('settings/teams')

    def plans(self):
        return self.view.render('settings/plans')

    def index(self):
        """ Show an individual setting """
        pass

    def create(self):
        """ """
        pass

    def store(self):
        """ Save a setting """
        pass

    def edit(self):
        """ Edit a setting """
        pass

    def update(self):
        """ Update a setting """
        pass

    def destroy(self):
        """ Delete a setting """
        pass
