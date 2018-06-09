''' Application Settings '''

import os

'''
|--------------------------------------------------------------------------
| Application Name
|--------------------------------------------------------------------------
|
| This value is the name of your application. This value is used when the
| framework needs to place the application's name in a notification or
| any other location as required by the application or its packages.
|
'''

NAME = 'Masonite 1.3'

'''
|--------------------------------------------------------------------------
| Application Debug Mode
|--------------------------------------------------------------------------
|
| When your application is in debug mode, detailed error messages with
| stack traces will be shown on every error that occurs within your
| application. If disabled, a simple generic error page is shown
|
'''

DEBUG = os.getenv('APP_DEBUG', False)

'''
|--------------------------------------------------------------------------
| Secret Key
|--------------------------------------------------------------------------
|
| This key is used to encrypt and decrypt various values. Out of the box
| Masonite uses this key to encrypt or decrypt cookies so you can use
| it to encrypt and decrypt various values using the Masonite Sign
| class. Read the documentation on Encryption to find out how.
|
'''

KEY = os.environ.get('KEY')

'''
|--------------------------------------------------------------------------
| Application URL
|--------------------------------------------------------------------------
|
| Sets the root URL of the application. This is primarily used for testing
|
'''

URL = 'http://localhost:8000'

'''
|--------------------------------------------------------------------------
| Providers List
|--------------------------------------------------------------------------
|
| Providers are a simple way to remove or add functionality for Masonite
| The providers in this list are either ran on server start or when a
| request is made depending on the provider. Take some time to can
| learn more more about Service Providers in our documentation
|
'''

PROVIDERS = [
    # Framework Providers
    'masonite.providers.AppProvider.AppProvider',
    'app.providers.SessionProvider.SessionProvider',
    'masonite.providers.RouteProvider.RouteProvider',
    # 'entry.providers.ApiProvider.ApiProvider',
    'masonite.providers.RedirectionProvider.RedirectionProvider',
    'masonite.providers.StartResponseProvider.StartResponseProvider',
    'masonite.providers.SassProvider.SassProvider',
    'masonite.providers.WhitenoiseProvider.WhitenoiseProvider',

    # Optional Framework Providers
    'masonite.providers.MailProvider.MailProvider',
    'masonite.providers.UploadProvider.UploadProvider',
    'masonite.providers.ViewProvider.ViewProvider',
    'masonite.providers.HelpersProvider.HelpersProvider',
    'masonite.providers.QueueProvider.QueueProvider',
    'masonite.providers.BroadcastProvider.BroadcastProvider',
    'masonite.providers.CacheProvider.CacheProvider',
    'masonite.providers.CsrfProvider.CsrfProvider',

    # Third Party Providers
    'integrations.providers.IntegrationProvider.IntegrationProvider',
    'billing.providers.BillingProvider',
    'app.providers.SentryServiceProvider.SentryServiceProvider',
    'app.providers.UploadBackblazeProvider.UploadBackblazeProvider',

    # Application Providers
    'app.providers.UserModelProvider.UserModelProvider',
    'app.providers.MiddlewareProvider.MiddlewareProvider',
]

'''
|--------------------------------------------------------------------------
| Base Directory
|--------------------------------------------------------------------------
|
| Sets the root path of your project
|
'''

BASE_DIRECTORY = os.getcwd()

'''
|--------------------------------------------------------------------------
| Static Root
|--------------------------------------------------------------------------
|
| Set the static root of your application that you wil use to store assets
|
'''

STATIC_ROOT = os.path.join(BASE_DIRECTORY, 'storage')
