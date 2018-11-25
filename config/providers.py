""" Providers Configuration File """

from billing.providers import BillingProvider
# from dashboard.providers import DashboardProvider, UserManagementProvider
from masonite.providers import (AppProvider, BroadcastProvider, CacheProvider,
                                CsrfProvider, HelpersProvider, MailProvider,
                                QueueProvider, RouteProvider, SassProvider,
                                SessionProvider,
                                StatusCodeProvider, UploadProvider,
                                ViewProvider, WhitenoiseProvider)
from masonite_heroku.providers import DeployProvider
from notifications.providers import NotificationProvider
from app.providers import (MiddlewareProvider, SentryServiceProvider,
                           UserModelProvider)
from events.providers import EventProvider

"""
|--------------------------------------------------------------------------
| Providers List
|--------------------------------------------------------------------------
|
| Providers are a simple way to remove or add functionality for Masonite
| The providers in this list are either ran on server start or when a
| request is made depending on the provider. Take some time to can
| learn more more about Service Providers in our documentation
|
"""

PROVIDERS = [
    # Framework Providers
    AppProvider,
    SessionProvider,
    RouteProvider,
    StatusCodeProvider,
    # StartResponseProvider,
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
    # DashboardProvider,
    # UserManagementProvider,
    DeployProvider,
    NotificationProvider,
    EventProvider,

    # Application Providers
    UserModelProvider,
    MiddlewareProvider
]
