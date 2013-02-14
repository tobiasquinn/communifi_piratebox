#PirateBox Notes

Installed newest openwrt trunk snapshot (11/Feb/2012)

Change LAN interface to be home LAN ip range (static 192.168.0.111)

Wireless doesn't seem to be present (not enabled?)

Power off, remove usb drive

Copy files from vfat created usb drive. Reformat drive as vfat partition first, additional ext4 partition, place files from vfat back on usb, startup...

Setup mount points in piratebox.

Add these lines to /etc/config/fstab

	config mount
		option target '/mnt/home'
		option device '/dev/sda2'
		option fstype 'ext4'
		option options 'rw,sync'
		option enabled '1'
		option enabled_fsck '1'

Reboot and this now allows a proper user to be added with unix permissions

## Path setup

add these two lines to /etc/profile to allow library paths etc.
	
	export LD_LIBRARY_PATH=/lib:/usr/lib:/usr/local/lib 
	export PATH=$PATH:/mnt/ext/usr/sbin:/mnt/ext/usr/bin

## Development Packages

Install with:

	opkg install <pkg>

###shadow-useradd

Use to add a non privileged user, also make home dir:

	useradd xxx
	mkdir -p /mnt/home/xxx
	chown xxx /mnt/home/xxx

###sudo

use visudo to add user xxx to the sudoers file (seems to be crash on sudo with shell)

now use

	opkg -d piratebox install <pkg>

###python

download setuptools from pypi (the egg file for 2.7)

login as root: sh setuptools-0.6c11-py2.7.egg

adds easy_install, use easy_install to install virtualenv

add a python environment, login as xxx user:

	virtualenv venv
	source venv/bin/activate

###flask

pip install flask

###git

opkg -d piratebox install git
