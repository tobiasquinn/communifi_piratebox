#Packaging webapps for PirateBox

Tobias Quinn <tobias@tobiasquinn.com>

This focusses on PirateBoxes that run OpenWRT.

##Aims

To provide a method to allow developers to create web apps that can be run on a PirateBox.

To provide PirateBox users with an easy way to choose a selection of web apps to be run on a PirateBox.

##Web apps

What is needed for a useful web app.

###Server

####Needed
* Ability to serve files to clients
* Persistent storage 
####Would be nice
* Realtime server<->client connections

##Ideas

This is very python based as I am familiar with it and it's available on all platforms likely to be used by end users for development eg. Linux, Mac, Windows. It also has well documented interfaces, and it's performance as a server seems reasonable on the OpenWRT PirateBox I've been testing (WR703N).

Tornado is a lightweight non-blocking web server that can support websockets allowing connected realtime client sessions. It is also capable of running WSGI applications.

This would provide a python based environment to develop web applications in. WSGI is a well defined standard allowing python server application to be run within a standard environment.

Frameworks such as flask, bottle and django are based around WSGI.

[opkg](http://code.google.com/p/opkg/) is the package format used by OpenWRT and the PirateBox framework. It is simple enough to setup a repository this post has references and details [OPKG Repository Server Setup](https://groups.google.com/forum/#!topic/opkg-devel/yLg8vyxClow).

This could be used to setup a standard server and service that would run on PirateBox start. This would provide a server framework which would then have a configuration file in /etc which would define things like which port to run on.

A standard way of setting up apps to be managed and run by this server would be to have configuration files that point to the appropriate python modules to run with a desired path for the server. Something like this

	[Voting App]
	routes=communifi.webapps.votecount.routes
	name="Voting Demo"
	version=1
	description="A Vote Counting Demonstration Application"

This would allow the server to assemble applications to run at startup and serve these from a single port. Currently supported PirateBox applications can probably be supported in this way as well.

The server could construct a page that lists the available application to the user. A click would open the appropriate application.

##What we would provide

An opkg repository and instructions on how to add this to a PirateBox install.

Server application.

Service packages which provide standard services a webapp may require such as persistent session management, database/file storage, sockjs implementation etc.

Example webapps. Approved by us webapps eg. chat, voting, whatever we think of.

Documentation to allow webapps to be written at various levels.