#!/usr/bin/env python
import tornado.ioloop
import tornado.web
from sockjs.tornado import SockJSRouter, SockJSConnection

PORT=6001
SIO_PORT = PORT + 1

class VoteConnection(SockJSConnection):
    _voters = set()
    _voters_votes = {}
    _candidates = []

    def on_open(self, request):
        print request
        # pass the candidates in using the request object
        print "connection init", id(self)
        self._voters.add(self)
        #self._candidates = self.request

    def disconnect(self, *args, **kwargs):
        print "disconnect", args, kwargs
        print "disc", id(self)
        self._voters.remove(self)
        self._voteinfo()

    def _voteinfo(self):
        total_votes = {}
        # sum the votes
        for vote in self._voters_votes.values():
            try:
                total_votes[vote] += 1
            except KeyError:
                total_votes[vote] = 1
        self.broadcast(self._voters, {'voteinfo': {
            'voters': len(self._voters),
            'votes': total_votes
        }})

    def on_connect(self, data):
        # send the candidate information
        print "CONNECT", self._candidates
        self.send({'candidates': self._candidates})

    def on_vote(self, data):
        self._voters_votes[id(self)] = data
        self._voteinfo()

    def on_message(self, mess):
        print "ON_MESSAGE", mess

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render('app/index.html')

VoteRouter = SockJSRouter(VoteConnection, '/vote')
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
