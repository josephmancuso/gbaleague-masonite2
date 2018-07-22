""" Providers Configuration File """

from masonite.providers import (
    AppProvider, SessionProvider, RouteProvider,
    StatusCodeProvider, StartResponseProvider,
    SassProvider, WhitenoiseProvider, MailProvider,
    UploadProvider, ViewProvider, HelpersProvider,
    QueueProvider, BroadcastProvider, CacheProvider,
    CsrfProvider,
)

from billing.providers import BillingProvider
from dashboard.providers import DashboardProvider
from app.providers.MiddlewareProvider import MiddlewareProvider
from app.providers.SentryServiceProvider import SentryServiceProvider
from app.providers.UserModelProvider import UserModelProvider
from app.providers.AppEventProvider import AppEventProvider
from dashboard.providers import UserManagementProvider
from masonite_heroku.providers import DeployProvider

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
    AppProvider,
    SessionProvider,
    RouteProvider,
    StatusCodeProvider,
    StartResponseProvider,
    WhitenoiseProvider,
    ViewProvider,
    HelpersProvider,

    # Optional Framework Providers

    SassProvider,
    MailProvider,
    UploadProvider,
    QueueProvider,
    CacheProvider,
    BroadcastProvider,
    CacheProvider,
    CsrfProvider,

    # Third Party Providers
    BillingProvider,
    SentryServiceProvider,
    DashboardProvider,
    UserManagementProvider,
    DeployProvider,

    # Application Providers
    UserModelProvider,
    MiddlewareProvider,
    AppEventProvider,
]
