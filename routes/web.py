''' Web Routes '''
from masonite.routes import Get, RouteGroup
from masonite.helpers.routes import get, post
from dashboard.routes import routes as DashboardRoutes
from dashboard.routes import management_routes

ROUTES = [

    RouteGroup([
        get('/discover', 'WelcomeController@discover').name('discover'),
        get('/', 'WelcomeController@show').name('home'),
    ]),

    # League Routes
    RouteGroup([
        get('/@id', 'LeagueController@show').name('id'),
        get('/@id/teams', 'LeagueController@teams').name('teams'),
        get('/@id/draft', 'DraftController@show').name('draft'),
        get('/@id/join', 'LeagueController@join').name('join'),

        # Scheduling
        get('/@id/schedule', 'ScheduleController@show').name('schedule'),

        # League Owner Routes
        RouteGroup([
            post('/@id/add-schedule', 'ScheduleController@store'),
            post('/@id/delete', 'LeagueController@delete').name('delete'),
            post('/@id/remove-schedule', 'ScheduleController@delete'),
            get('/@id/requests', 'RequestController@show').name('requests'),
            get('/@id/edit', 'LeagueController@edit').name('edit'),
            post('/@id/edit', 'LeagueController@store_edit').name('edit.store'),
        ], middleware=('auth', 'league.owner',)),

        # League Member Routes
        RouteGroup([
            post('/@id/draft', 'DraftController@draft'),
            post('/@id/status', 'DraftController@status'),
            post('/@id/skip', 'LeagueController@skip'),
        ], middleware=('auth',)),

        # League App Integrations
        get('/@id/apps', 'AppIntegrationsController@show').name('apps'),
    ], prefix="/league", name="league."),

    RouteGroup([
        get('/team', 'TeamController@show').name('teams'),
        post('/team', 'TeamController@store').name('create-team'),

        get('/league', 'LeagueController@create').name('create-league').name('leagues'),
        post('/league', 'LeagueController@store'),
    ], prefix='/create', name="create.", middleware=('auth',)),

    # Premium
    RouteGroup([
        get('', 'PremiumController@show'),
        post('', 'PremiumController@store'),
        post('/swap', 'PremiumController@update'),
        post('/cancel', 'PremiumController@delete'),
    ], prefix="/leaguepass"),

    # Authentication
    RouteGroup([
        get('/login', 'LoginController@show').name('login'),
        get('/logout', 'LoginController@logout'),
        post('/login', 'LoginController@store'),
        get('/register', 'RegisterController@show'),
        post('/register', 'RegisterController@store'),
        get('/home', 'HomeController@show'),
    ]),

    post('/add-team', 'RequestController@store'),
    post('/handle-team-request', 'RequestController@handle'),

    # Slack
    get('/integration/slack/@id', 'AppIntegrationsController@slack_send'),
    Get().domain('*').route('/oauth/slack', 'AppIntegrationsController@slack_return'),

    # Discord
    get('/integration/discord/@id', 'AppIntegrationsController@discord_send'),
    Get().domain('*').route('/oauth/discord', 'AppIntegrationsController@discord_return'),
    Get().domain('*').route('/slacktest', 'WelcomeController@slack').name('create-league'),

    # Testing
    post('/stripe/webhook', '/billing.controllers.WebhookController@handle').domain('684b1285'),
    management_routes(),
]

ROUTES += DashboardRoutes()
