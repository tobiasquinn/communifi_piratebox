#!/usr/bin/env python
import tornado.ioloop
import tornado.web

PORT=6001

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render('app/index.html')

application = tornado.web.Application([
    (r"/",      IndexHandler),
    (r"/(.*)",  tornado.web.StaticFileHandler, {"path": "app"}),
])

if __name__ == "__main__":
    print "Server start port %d" % (PORT)
    application.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()
