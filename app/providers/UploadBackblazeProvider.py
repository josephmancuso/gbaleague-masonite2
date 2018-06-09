''' A UploadBackblazeProvider Service Provider '''
from masonite.provider import ServiceProvider
from ..helpers.UploadBackblazeDriver import UploadBackblazeDriver

class UploadBackblazeProvider(ServiceProvider):

    wsgi = False

    def register(self):
        self.app.bind('UploadBackblazeDriver', UploadBackblazeDriver)

    def boot(self):
        pass
