#VoteCount

##A simple vote counting demonstration webapp using sockjs-tornado and angularjs

sockjs is used as a websocket emulation, the message are send in json format as a dict of message type and payload eg:

	{'voteinfo': {'votes': 2, 'expected': 5}}

Here voteinfo is the message type, the payload is a dictionary of values.

A message with no payload is not json encoded, just send as a string eg:

'connect'

Here connect is the message type, there is no payload.

###angular.js service

A rudimentry service is provide so that messages are dispatched to and from the controller by message type. The interface is:

	socket is the service name
	
	socket.onopen() - called on sockjs connection open
	socket.on(messagetype, callback) - callback is called when message of type messagetype is received
	socket.emit(messagetype, [data]) - send message of messagetype with optional data
