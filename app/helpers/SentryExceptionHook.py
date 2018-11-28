from config import application

class SentryExceptionHook:

    def load(self, container):
        if not application.DEBUG:
            from raven import Client
            client = Client(
                'https://7b9f4b2052ff4a43a689d2597250f8a4:4b435a4c2f7d461b81a356a81477a396@sentry.io/1198997')
            client.user_context({
                'url': container.make('Request').path,
                'user': container.make('Request').user().email if container.make('Request').user() else None
            })
            client.captureException()