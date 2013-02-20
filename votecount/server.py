#!/usr/bin/env python
import tornado.ioloop
import tornado.web
from sockjs.tornado import SockJSRouter
import logging
logging.getLogger().setLevel(logging.DEBUG)
from servers.votecount import VoteConnection

PORT=6001
SIO_PORT = PORT + 1

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render('app/index.html')

VoteRouter = SockJSRouter(VoteConnection, '/vote', {'candidates': ['YES', 'NEUTRAL', 'NO']})
#print VoteRouter.urls
application = tornado.web.Application(VoteRouter.urls +
    [
        (r"/",      IndexHandler),
        (r"/(.*)",  tornado.web.StaticFileHandler, {"path": "app"})
    ]
)

if __name__ == "__main__":
    print "Server start port %d" % (PORT)
    application.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()
