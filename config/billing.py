''' Masonite Billing Settings '''

import os

'''
|--------------------------------------------------------------------------
| Billing Processor Driver
|--------------------------------------------------------------------------
|
| This is the default driver that your application will use for payments.
| You can add any drivers you need to Masonite if they exist. Although
| Masonite Billing currently only comes with the 'stripe' driver.
|
| Supported: 'stripe'
|
'''

DRIVER = 'stripe'

'''
|--------------------------------------------------------------------------
| Billing Processor Driver Configuration
|--------------------------------------------------------------------------
|
| Put any configurations required for the driver. The key in the dictionary
| should be the name of a driver with a dictionary of configurations.
|
'''

DRIVERS = {
    'stripe': {
        'client': os.getenv('STRIPE_CLIENT'),
        'secret': os.getenv('STRIPE_SECRET'),
        'currency': 'usd',
    }
}
