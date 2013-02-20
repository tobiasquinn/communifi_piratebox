###PirateBox Technical Overview

Tobias Quinn <tobias@tobiasquinn.com>

My current technical understanding of what a WR703N based PirateBox is:

It's an OpenWRT based system which has a convenience layer called PirateBox which consists of three logical portions:

1. Storage portion - these are scripts and configurations that add USB storage services and configuration overlays to OpenWRT on boot.

2. Services portion - this is a mix of OpenWRT configuration and services that are started at boot to configure provide things like wifi access point, routing, DNS services.

3. Application portion - This is the main user visible section of the PirateBox project which provides a web interface to some of the storage portion, forum and chat interface.

The boundary layers between these portions are bound up into one coherent entity - the PirateBox scripts and bootstrapping information can be found at [PirateBox_DIY_OpenWrt](http://daviddarts.com/piratebox-diy-openwrt/?title=PirateBox_DIY_OpenWrt).