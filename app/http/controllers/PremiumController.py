''' A Module Description '''

class PremiumController:
    ''' Class Docstring Description '''

    def show(self):
        print(auth().is_subscribed())
        return view('leaguepass')
    
    def store(self):
        # subscribe user
        request().user().subscribe(request().input('plan'), request().input('token'))

        # redirect back
        return request().redirect('/leaguepass')

    def update(self):
        request().user().swap(
            request().input('plan')
        )
        return request().redirect('/leaguepass')

    def delete(self):
        request().user().cancel(now=True)

        return request().redirect('/leaguepass')