''' A Module Description '''

class PremiumController:
    ''' Class Docstring Description '''

    def show(self):
        return view('leaguepass')
    
    def store(self):
        # subscribe user
        request().user().subscribe(request().input('plan'), request().input('stripeToken'))

        # redirect back
        return request().back()

    def update(self):
        request().user().swap(
            request().input('plan')
        )
        return request().redirect_to('settings.plans')

    def delete(self):
        request().user().cancel(now=False)

        return request().redirect_to('settings.plans')

    def resume(self):
        request().user().resume()

        return request().redirect_to('settings.plans')