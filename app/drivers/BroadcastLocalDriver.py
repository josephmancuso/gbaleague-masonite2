from masonite.drivers import BaseDriver
from config import broadcast
import asyncio
import json


class BroadcastLocalDriver(BaseDriver):

    def __init__(self):
        """Broadcast driver for sending local websockets.

        Arguments:
            BroadcastConfig {config.broadcast} -- Broadcast configuration.
        """
        self.config = broadcast
        self.ssl_message = True

    def ssl(self, boolean):
        """Set whether to send data with SSL enabled.

        Arguments:
            boolean {bool} -- Boolean on whether to set SSL.

        Returns:
            self
        """
        self.ssl_message = boolean
        return self

    def channel(self, channels, message, event='base-event'):
        """Specify which channel(s) you want to send information to.

        Arguments:
            channels {string|list} -- Can be a string for the channel or a list of strings for the channels.
            message {string} -- The message you want to send to the channel(s)

        Keyword Arguments:
            event {string} -- The event you want broadcasted along with your data. (default: {'base-event'})

        Raises:
            DriverLibraryNotFound -- Thrown when pusher is not installed.

        Returns:
            string -- Returns the message sent.
        """
        try:
            import websockets
        except ImportError:
            raise DriverLibraryNotFound(
                'Could not find the "websockets" library. Please pip install this library running "pip install websockets"')

        async def hello():
            async with websockets.connect(
                    'ws://localhost:9001') as websocket:

                await websocket.send(json.dumps({'channel': channels, 'message': message, 'event': event}))
        
        asyncio.get_event_loop().run_until_complete(hello())

        return message
