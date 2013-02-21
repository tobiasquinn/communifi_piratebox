from tornado.web import StaticFileHandler, RequestHandler
from communifi.server.routes import Routes
print "IMPORT MWMWMWM"
class IndexHandler(RequestHandler):
    def get(self):
        return self.render('app/index.html')

# FIXME make this prefix set by webapp runner
Routes([
    (r"/vote",      IndexHandler),
    (r"/vote/(.*)",  StaticFileHandler, {"path": "app"})
])
