from sockjs.tornado import SockJSConnection
import logging, json

class VoteConnection(SockJSConnection):
    _voters = set()
    _voters_votes = {}
    _candidates = []

    def on_open(self, request):
        logging.info("VoteConnection::on_open IP is (%s)" % (request.ip))
        # pass the candidates in using the request object
        self._voters.add(self)
        #self._candidates = self.request
        self._candidates = ['YES', 'NO', 'MAYBE']

    def on_close(self):
        print "disconnect"
        self._voters.remove(self)
        self._voteinfo()

    # simple message dispatcher calls on_xxx methods for xxx message type
    def on_message(self, mess):
        print "ON_MESSAGE", mess
        method = json.loads(mess)
        func = getattr(self, "on_%s" % (method['name']))
        try:
            data = method['data']
        except KeyError:
            data = None
        func(data)

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
        self._voteinfo()

    def on_vote(self, data):
        self._voters_votes[id(self)] = data
        self._voteinfo()
