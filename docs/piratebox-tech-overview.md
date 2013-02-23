###PirateBox Technical Overview

Tobias Quinn <tobias@tobiasquinn.com>

My current technical understanding of what a WR703N based PirateBox is:

It's an OpenWRT based system which has a convenience layer called PirateBox which consists of three logical portions:

1. Storage portion - these are scripts and configurations that add USB storage services and configuration overlays to OpenWRT on boot.

2. Services portion - this is a mix of OpenWRT configuration and services that are started at boot to configure provide things like wifi access point, routing, DNS services.

3. Application portion - This is the main user visible section of the PirateBox project which provides a web interface to some of the storage portion, forum and chat interface.

The boundary layers between these portions are bound up into one coherent entity - the PirateBox scripts and bootstrapping information can be found at [PirateBox_DIY_OpenWrt](http://daviddarts.com/piratebox-diy-openwrt/?title=PirateBox_DIY_OpenWrt).

Networking Notes
================

Graham Lally <scribe@exmosis.net>

Looking into how the networking works is a little convoluted. Notes below will be updated as a I find out more.

I'm primarily looking into how DNS and DHCP are handled. I _think_ we want something like this:

- The main domain name of the box itself (eg. piratebox.lan by default, but propose _yourchoice_.cb (CB = communifi box)) should resolve to the IP of the Piratebox (eg. 192.168.1.1 in my case)
- Everything else (for now) should resolve using the upstream wired connection, eg. 192.168.1.254 in my case

The easiest way to do this is to tell clients to use the box (eg. 192.168.1.1) as DNS, then get dnsmasq (the DNS/DHCP server running on the PB) to resolve as per above.

Currently the PB dnsmasq config files are generated on startup, combining a "static" file (/opt/piratebox/conf/dnsmasq\_default.conf) with some dynamic values to create /opt/piratebox/conf/dnsmasq\_generated.conf. By default, I think this:

1. Ignores /etc/resolv.conf
2. Ignores /etc/hosts
3. Redirects all lookups to resolve to the PB (using "address=/#/192.168.1.1")

*Current problem 1:* Confusion between what's being handled by dnsmasq and what's being listened to in /etc/resolv.conf, /etc/config/network and /etc/dhcp

*Current problem 2:* OSX doesn't seem to update with latest dns settings when re-connecting to the box, including IP within specified range. Wondering if dnsmasq is actually just proxying DHCP to the wired router?


