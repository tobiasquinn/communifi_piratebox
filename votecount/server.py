#!/usr/bin/env python
from flask import Flask, render_template, send_file, jsonify, request, Response
from socketio import socketio_manage
from socketio.namespace import BaseNamespace
from socketio.mixins import BroadcastMixin
import random
app = Flask(__name__)

class VoteNamespace(BaseNamespace, BroadcastMixin):
    _voters = {}
    _voters_votes = {}
    _candidates = []

    def initialize(self):
        # pass the candidates in using the request object
        print "connection init", id(self)
        self._voters.add(self)
        #self._candidates = self.request
        self._candidates = ['YES', 'NO', 'MAYBE']

    def disconnect(self, *args, **kwargs):
        print "disconnect", args, kwargs
        print "disc", id(self)
        del self._voters[id(self)]
        super(VoteNamespace, self).disconnect(*args, **kwargs)
        self._voteinfo()

    # simpe message dispatcher calls on_xxx methods for xxx message type
    def on_message(self, mess):
        print "ON_MESSAGE", mess
        method = getattr(self, "on_%s" % (mess))
        print "METHOD", method
        method("TESTING")

    def _voteinfo(self):
        total_votes = {}
        # sum the votes
        for vote in self._voters_votes.values():
            try:
                total_votes[vote] += 1
            except KeyError:
                total_votes[vote] = 1
        self.broadcast_event('voteinfo', {
            'voters': len(self._voters),
            'votes': total_votes
        })

    def on_connect(self, data):
        # send the candidate information
        print "CONNECT", self._candidates
        self.emit('candidates', self._candidates)

    def on_vote(self, data):
        self._voters_votes[id(self)] = data
        self._voteinfo()

<<<<<<< Updated upstream
@app.route('/', defaults={'path': '/index.html'})
@app.route('/<path:path>')
def catch_all(path):
    return send_file('app/%s' % (path))

@app.route('/votingtime')
def votingtime():
    return jsonify(time=-1)
    #return jsonify(time=random.randint(10,50))
=======
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render('app/index.html')
>>>>>>> Stashed changes

@app.route('/socket.io/<path:path>')
def run_socketio(path):
    payload = ["UP", "NEUTRAL", "DOWN"]
    socketio_manage(request.environ, {'/vote': VoteNamespace}, request=payload)
    return Response()

if __name__ == '__main__':
    app.debug = True
    print app.url_map
    from socketio.server import SocketIOServer
    SocketIOServer(('0.0.0.0', 6001), app,
            resource="socket.io", policy_server=False).serve_forever()
    #app.run(host='0.0.0.0', port=6001)
