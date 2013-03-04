Notes on setting up DNS and DHCP
================================

This document sets out the steps and edits needed to a standard Piratebox install to get it to route traffic through a wired connection _except_ a chosen domain (eg communifi.cb).

Tested on a TP-LINK MR3040.

## /etc/config/network

/etc/config/network needs to be setup to create the correct resolv configuration. This may be the default, need to check, but I basically use a single DNS (Google's, situated at 8.8.8.8) for DNS.

```
config interface 'loopback'
  option ifname 'lo'
	option proto 'static'
	option ipaddr '127.0.0.1'
	option netmask '255.0.0.0'

config interface 'lan'
	option ifname 'eth0'
	option type 'bridge'
	option proto 'static'
	option netmask '255.255.255.0'
	option gateway '192.168.1.254' <- needs updating to router address
	option ipaddr '192.168.1.1'
	option dns '8.8.8.8'  <- Use Google for DNS
```

This puts Google's DNS into /etc/resolv.conf when we start the box, which we'll use for clients looking up all domains except the ones we intercept later.
We could probably set dns to the router address if wanted, or some other accessible server.

## Piratebox config

By default, the Piratebox ignores all the DNS setup in /etc, using its own dnsmasq config to intercept _all_ DNS requests, and re-point them at the box itself. To get out around this, we need to edit the config scripts a bit:

1. Edit /opt/piratebox/conf/dnsmasq_default.conf to remove the 'no-resolv' setting:

    # no-resolv

(This was the second line in my version.) This tells dnsmasq to use the 8.8.8.8 DNS server we specified above. This file is added to to generate the actual PB config file used - see next step.

2. Edit /opt/piratebox/bin/generate_config_files.sh to only intercept the domain(s) we want to. Change this line:

    dns_redirect="/#/$net.$ip_pb"

to

    dns_redirect="/piratebox.lan/$net.$ip_pb"

where "piratebox.lan" is the domain you want to use.

(I _think_ we might be able to intercept a TLD here, eg *.cb, by using /cb/, but need to test.)

## IPTables

Finally, we need to stop clients from getting their DHCP from upstream (ie from the router the PB is connected to). We can do this using iptables, which is disabled by default.

Edit /etc/sysctl.conf to enable iptables. Comment out the last line:

    # net.bridge.bridge-nf-call-iptables=0

Then allow all traffic through, via this command (which needs to be added somewhere in the startup scripts, otherwise you'll need to run it on every restart):

    iptables -I zone_wan_ACCEPT -j ACCEPT

## DNS interception

So far this is all fine if clients are accepting DNS setup via DHCP from the box. If they're overriding DNS by using their own settings, I don't think they see the box properly. With iptables enabled, we should be able to intercept all DNS requests, but not figured this out yet...

Should be _something_ like:

    iptables -t nat -I PREROUTING -i wlan0 -p udp --dport 53 -j DNAT --to 192.168.1.1

