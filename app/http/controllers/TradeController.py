''' A Module Description '''
from app.League import League


class TradeController:
    ''' Class Docstring Description '''

    def show(self):
        league = League.find(request().param('id'))

        return view('leagues/trade', {'league': league})

    def store(self):
        league = League.find(request().param('id'))

        # add to trade table
