''' Database Settings '''

from masonite import env

from dotenv import find_dotenv, load_dotenv
from orator import DatabaseManager, Model

'''
|--------------------------------------------------------------------------
| Load Environment Variables
|--------------------------------------------------------------------------
|
| Loads in the environment variables when this page is imported.
|
'''

load_dotenv(find_dotenv())

'''
|--------------------------------------------------------------------------
| Database Settings
|--------------------------------------------------------------------------
|
| Set connection database settings here as a dictionary. Follow the
| format below to create additional connection settings.
|
| @see Orator migrations documentation for more info
|
'''

DATABASES = {
    'default': {
        'driver': env('DB_DRIVER'),
        'host': env('DB_HOST'),
        'database': env('DB_DATABASE'),
        'user': env('DB_USERNAME'),
        'password': env('DB_PASSWORD'),
        'prefix': ''
    }
}

DB = DatabaseManager(DATABASES)
Model.set_connection_resolver(DB)
