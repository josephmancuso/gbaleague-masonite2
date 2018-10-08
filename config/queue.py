''' Queue Settings '''

import os

'''
|--------------------------------------------------------------------------
| Queue Driver
|--------------------------------------------------------------------------
|
| Queues are an excellent way to send intensive and time consuming tasks
| into the background to improve performance of your application.
|
| Supported: 'async', 'amqp'
|
'''

DRIVER = os.getenv('QUEUE_DRIVER', 'async')

'''
|--------------------------------------------------------------------------
| Queue Drivers
|--------------------------------------------------------------------------
|
| Put any configuration settings for your drivers in this configuration
| setting.
|
'''

DRIVERS = {
    'amqp': {
        'username': os.getenv('QUEUE_USERNAME', 'guest'),
        'password': os.getenv('QUEUE_PASSWORD', 'guest'),
        'host': os.getenv('QUEUE_HOST', 'localhost'),
        'port': os.getenv('QUEUE_PORT', '5672'),
        'channel': os.getenv('QUEUE_CHANNEL', 'default'),
    }
}
