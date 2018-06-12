''' Web Routes '''
from masonite.routes import Get, Post
from masonite.helpers.routes import get, post, group
from dashboard.routes import routes as DashboardRoutes

ROUTES = [
    get('/', 'WelcomeController@show').name('home').middleware('auth'),
    get('/', 'WelcomeController@show').domain('*').name('home'),
    get('/', 'WelcomeController@show').domain('evening-ravine-84143').name('home'),
    get('/', 'WelcomeController@show').domain('evening-ravine-84143.herokuapp').name('home'),
    get('/discover', 'WelcomeController@discover').name('discover'),

    # group('/dashboard', [
    #     get('/user/@id', 'WelcomeController@discover').name('discover'),
    #     get('/test', 'WelcomeController@discover').name('discover'),
    # ]),


    get('/league/@id', 'LeagueController@show').name('league'),
    get('/league/@id/teams', 'LeagueController@teams').name('league-teams'),
    get('/league/@id/draft', 'DraftController@show').name('league-draft'),
    post('/league/@id/draft', 'DraftController@draft'),
    post('/league/@id/status', 'DraftController@status'),
    post('/league/@id/skip', 'LeagueController@skip'),

    # Joining Leagues
    get('/league/@id/join', 'LeagueController@join'),
    post('/add-team', 'RequestController@store'),

    # Scheduling
    get('/league/@id/schedule', 'ScheduleController@show'),
    post('/league/@id/add-schedule', 'ScheduleController@store'),
    post('/league/@id/remove-schedule', 'ScheduleController@delete'),

    get('/league/@id/trade', 'TradeController@show'),
    post('/league/@id/trade', 'TradeController@store'),

    # League Requests
    get('/league/@id/requests', 'RequestController@show'),
    post('/handle-team-request', 'RequestController@handle'),

    # League App Integrations
    get('/league/@id/apps', 'AppIntegrationsController@show'),

    # Slack
    get('/integration/slack/@id', 'AppIntegrationsController@slack_send'),
    Get().domain('*').route('/oauth/slack', 'AppIntegrationsController@slack_return'),

    # Discord
    get('/integration/discord/@id', 'AppIntegrationsController@discord_send'),
    Get().domain('*').route('/oauth/discord', 'AppIntegrationsController@discord_return'),
    # get('/oauth/discord', 'AppIntegrationsController@show'),

    get('/create/team', 'TeamController@show').name('create-team'),
    post('/create/team', 'TeamController@store').name('create-team'),

    get('/create/league', 'LeagueController@create').name('create-league'),
    post('/create/league', 'LeagueController@store'),

    Get().domain('*').route('/slacktest', 'WelcomeController@slack').name('create-league'),

    # Premium
    get('/leaguepass', 'PremiumController@show'),
    post('/leaguepass', 'PremiumController@store'),
    post('/leaguepass/swap', 'PremiumController@update'),
    post('/leaguepass/cancel', 'PremiumController@delete'),


    # Testing
    post('/stripe/webhook', '/billing.controllers.WebhookController@handle').domain('684b1285')
]

ROUTES += [
    get('/login', 'LoginController@show').name('login'),
    get('/logout', 'LoginController@logout'),
    post('/login', 'LoginController@store'),
    get('/register', 'RegisterController@show'),
    post('/register', 'RegisterController@store'),
    get('/home', 'HomeController@show'),
]

ROUTES += DashboardRoutes()

print(ROUTES)