class SentryExceptionHook:

    def load(self, container):
        from raven import Client
        client = Client(
            'https://7b9f4b2052ff4a43a689d2597250f8a4:4b435a4c2f7d461b81a356a81477a396@sentry.io/1198997')
        if container.make('Application').DEBUG == 'False':
            client.captureException()
