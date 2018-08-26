import htmlmin

class HtmlMinifyMiddleware:

    def __init__(self, Request):
        self.request = Request

    def after(self):
        if isinstance(self.request.app().make('Response'), str):
            self.request.app().bind(
                'Response',
                htmlmin.minify(
                    self.request.app().make('Response')
                )
            )
