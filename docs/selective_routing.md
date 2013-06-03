# Notes on setting up DNS and DHCP


This document sets out the steps and edits needed to a standard Piratebox install to get it to route traffic through a wired connection _except_ a chosen domain (eg communifi.cb).

Tested on a TP-LINK MR3040 running PB 0.6.3.

/etc/config/network only needs to be set up to get the piratebox packages, so if you've installed the PB already via http, then nothing needed here.

1. Add external DNS to PB for use by DHCP clients connecting, by
adding this to /etc/piratebox.common alongside the "nameserver
127.0.0.1" line:

  echo "nameserver 192.168.1.254" >> /tmp/resolv.conf

Were 192.168.1.254 is your router IP. Alternatively, use Google's DNS (8.8.8.8) to avoid having to set this if you move the box.

2. Comment out the 'no-resolv' setting in
/opt/piratebox/conf/dnsmasq_default.conf to allow the box to use other
DNS servers (specified, I believe, in /etc/config/network as 'dns'
options):

 \# no-resolv

3. Amend the PB config generation script at
/opt/piratebox/bin/generate_config_files.sh to only redirect a single
domain name, changing:

  dns_redirect="/#/$net.$ip_pb"

to:

  dns_redirect="/piratebox.lan/$net.$ip_pb"

(Where "piratebox.lan" is the domain you want to use. This doesn't need to be .lan - I use "exmosis.cb")

4. Enable iptables by editing /etc/sysctl.conf and commenting out:

  net.bridge.bridge-nf-call-iptables=0
  
ie. change it to:

  # net.bridge.bridge-nf-call-iptables=0


5. I found I had to tell iptables to be permissive, as it seemed
locked down by default. I added this to /etc/firewall.user:

  iptables -I zone_wan_ACCEPT -j ACCEPT

6. Then disallow DHCP traffic through the PB so you don't get DHCP clashes with your router. Add this to
the /etc/firewall.user script too:

  iptables -I FORWARD -p udp --dport 67:68 --sport 67:68 -j DROP



## DNS interception

So far this is all fine if clients are accepting DNS setup via DHCP from the box. If they're overriding DNS by using their own settings, I don't think they see the box properly. With iptables enabled, we should be able to intercept all DNS requests, but not figured this out yet...

Should be _something_ like but can't get it to work yet:

    iptables -t nat -I PREROUTING -i wlan0 -p udp --dport 53 -j DNAT --to 192.168.1.1

