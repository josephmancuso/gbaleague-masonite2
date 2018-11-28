import htmlmin
from masonite.request import Request
from masonite.response import Response

class HtmlMinifyMiddleware:

    def __init__(self, request: Request, response: Response):
        self.request = request
        self.response = response

    def after(self):
        if self.request.header('Content-Type') and 'text/html' in self.request.header('Content-Type') and not self.request.header('Location'):
            self.response.view(
                htmlmin.minify(self.response.data())
            )
        
        self.request.header('Cache-Control', 'max-age=3600, must-revalidate', http_prefix=False)
