""" A BroadcastWorkCommand Command """
from cleo import Command
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

clients = []
class SimpleEcho(WebSocket):

    def handleMessage(self):
        print('> broadcasting:', self.data)
        for client in clients:
            client.sendMessage(self.data)

    def handleConnected(self):
        clients.append(self)

    def handleClose(self):
        clients.remove(self)


class BroadcastWorkCommand(Command):
    """
    Start a broadcasting websocket server

    broadcast:work
    """

    def handle(self):
        server = SimpleWebSocketServer('localhost', 9001, SimpleEcho)
        self.info('Server Started!')
        server.serveforever()
