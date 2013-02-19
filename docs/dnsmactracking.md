#DNS hijacking and DHCP user tracking

Tobias Quinn <tobias@tobiasquinn.com>

##DNS hijacking

It is expected that some users of the piratebox will require internet access as well as access to piratebox apps using a wifi connection. To allow easy access to apps on the piratebox, a standard DNS name server is made available. While the bonjour protocol is becoming more widespread in use for LAN dynamic DNS, it is still not present on a large number of used platforms.

It is possible to use a small DNS server on the piratebox (dnsmasq) which adds in a local address space (eg. piratebox.lan, piratebox.local etc.). When a client connecting to the piratebox access point is issued with an IP address, the dhcp client can choose to use the assigned DNS server IP or, they may have a custom DNS setup eg. OpenDNS or Googles DNS servers.

To tackle this it is possible to place dummy ethernet routes into the pirateboxes routing table which would intercept DNS requests to a known list of communly used and well known external DNS servers eg. 8.8.8.8 or 8.8.8.4 at the IP layer so that users with custom DNS settings can use piratebox apps with no client reconfiguration.

###Use cases

1) Bob connects to the piratebox and is isseued an IP address and DNS settings. Bobs client uses the DNS settings from the piratebox.

2) Bob connects to the piratebox with his custom DNS settings (eg. pointing to Googles server). Piratebox issues an IP address and DNS settings. Bobs client ignore the DNS settings. Piratebox intercepts DNS requests using the ethernet routes and Bob is able to access piratebox services using urls like piratebox.lan etc.

##Binding user sessions to MAC address

As we expect users of apps on the piratebox to connect over wifi and be issued with a dhcp by the piratebox it should be possible to bind user data held on the piratebox to the device that the user connects.

###Use Case

Bob connects for the first time to the piratebox. He is issued an ip address from the piratebox, at the web application layer the piratebox requests a nickname that Bob wishes to be known by. The web application stores the username with Bobs MAC address using the provided service. Bob does stuff, posts a hastily written but insightful political manifesto, disconnects and leaves.

Alice connects to the piratebox and sees the political manifesto from Bob, she is incensed and flies into almost uncontrollable rage. She replies to Bobs message inappropriately, but makes the step of adding a smiley at the end of the offensive rant.

Bob then returns to the location of the piratebox. He connects and is issued an ip address by the piratebox dhcp server, the piratebox recognises his MAC address in its database of known users. Applications then have access to stored information about Bob such as his chosen username and data that they may have stored using a provided service. For example, when Bob reconnects the an applciation informs him of Alices reply to his manifesto.