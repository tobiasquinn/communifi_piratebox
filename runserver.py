#!/usr/bin/env python
from communifi.server.webappserver import WebAppServer

SERVER_PORT = 6001

server = WebAppServer("config/webapps", port=6001)
server.start()
