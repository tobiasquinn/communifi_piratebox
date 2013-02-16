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

    def initialize(self):
        print "connection init", id(self)
        self._voters[id(self)] = self

    def disconnect(self, *args, **kwargs):
        print "disconnect", args, kwargs
        print "disc", id(self)
        del self._voters[id(self)]
        super(VoteNamespace, self).disconnect(*args, **kwargs)
        self._voteinfo()

    def _voteinfo(self):
        print "VOTER_VOTES", self._voters_votes
        total_votes = {}
        # sum the votes
        for vote in self._voters_votes.values():
            try:
                total_votes[vote] += 1
            except KeyError:
                total_votes[vote] = 1
        print "TOTAL_VOTES", total_votes
        self.broadcast_event('voteinfo', {
            'voters': len(self._voters),
            'votes': total_votes
        })

    def on_connect(self, data):
        self._voteinfo()

    def on_vote(self, data):
        self._voters_votes[id(self)] = data
        self._voteinfo()

@app.route('/', defaults={'path': '/index.html'})
@app.route('/<path:path>')
def catch_all(path):
    return send_file('app/%s' % (path))

@app.route('/votingtime')
def votingtime():
    return jsonify(time=-1)
    #return jsonify(time=random.randint(10,50))

@app.route('/socket.io/<path:path>')
def run_socketio(path):
    socketio_manage(request.environ, {'/vote': VoteNamespace})
    return Response()

if __name__ == '__main__':
    app.debug = True
    print app.url_map
    from socketio.server import SocketIOServer
    SocketIOServer(('0.0.0.0', 6001), app,
            namespace="socket.io", policy_server=False).serve_forever()
    #app.run(host='0.0.0.0', port=6001)
