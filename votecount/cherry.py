#!/usr/bin/env python
from cherrypy import wsgiserver
from server import app

d = wsgiserver.WSGIPathInfoDispatcher({'/': app})
server = wsgiserver.CherryPyWSGIServer(('0.0.0.0', 6001), d)

if __name__ == "__main__":
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()
