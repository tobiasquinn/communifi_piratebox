#!/usr/bin/env python
import tornado.ioloop
import tornado.web
from sockjs.tornado import SockJSRouter
import logging
logging.getLogger().setLevel(logging.DEBUG)
import ConfigParser

# This is a web app server that reads a .ini style configuration file
# [WebAppName]
# routes=communifi.webapps.xxx.routes # an object that describes to be added to the server
# name=xxx # Name for button to select app
# description=xxx # Description of the app

from tornado.template import Loader
import os

loader = Loader(os.path.dirname(os.path.realpath(__file__)) + os.sep + 'html')
class WebAppIndexHandler(tornado.web.RequestHandler):
    _apps = None

    @classmethod
    def setApps(self, apps):
        self._apps = apps

    def get(self):
        html = loader.load("index.html").generate(apps=self._apps)
        return self.write(html)

class WebAppServer:
    def __init__(self, configfile, port=6001):
        self._port = port
        # parse our configuration file
        config = ConfigParser.ConfigParser()
        config.read(configfile)
        self._apps = []
        for section in config.sections():
            app = {}
            app['name'] = section
            app['routes'] = config.get(section, 'routes')
            app['version'] = config.get(section, 'version')
            app['description'] = config.get(section, 'description')
            logging.info("WebAppServer found app:%s" % (app))
            self._apps.append(app)
        # load our apps into the webapp index handler for templating purposes
        WebAppIndexHandler.setApps(self._apps)

    def start(self):
        # FIXME: this should probably do some sort of sanity checking
        # our index page route
        server_routes = [(r"/", WebAppIndexHandler),]
        # assemble all our routes
        for app in self._apps:
            route = app['routes']
            print "ROUTE", route
            # the imported file attaches itself to the route module
            __import__(route)
        import routes
        # ask the routes module for routes it has collected
        server_routes += routes.routes()
        # Start the server
        logging.debug("WebAppServer routes:%s" % (server_routes))
        self._application = tornado.web.Application(server_routes)
        self._application.listen(self._port)
        logging.info("WebAppServer start on port %d" % (self._port))
        # Run forever
        tornado.ioloop.IOLoop.instance().start()

#class IndexHandler(tornado.web.RequestHandler):
#    def get(self):
#        return self.render('app/index.html')
#
#VoteRouter = SockJSRouter(VoteConnection, '/vote', {'candidates': ['YES', 'NEUTRAL', 'NO']})
##print VoteRouter.urls
#application = tornado.web.Application(VoteRouter.urls +
#    [
#        (r"/",      IndexHandler),
#        (r"/(.*)",  tornado.web.StaticFileHandler, {"path": "app"})
#    ]
#)
#
#if __name__ == "__main__":
#    print "Server start port %d" % (PORT)
#    application.listen(PORT)
#    tornado.ioloop.IOLoop.instance().start()
