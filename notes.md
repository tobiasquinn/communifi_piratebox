#PirateBox Notes

Installed newest openwrt trunk snapshot (11/Feb/2012)

Change LAN interface to be home LAN ip range (static 192.168.0.111)

Wireless - needs line in /etc/config/wireless changed:

	option mode 'sta'
	to:
	option mode 'ap'

Change ssid, encryption 'psk2' and key here as well if required.

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

## Upgrading firmware

Use the appropriate -sysupgrade image, the command in follow steps for normal piratebox install, starting from step x. Remeber to setup ip address in /etc/piratebox.common and run /etc/init.d/piratebox setup before rebooting.

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

note that git pull doesn't work, use git fetch then git merge

###screen

make sure terminfo is installed without -d piratebox.

Uninstall/reinstall if necessary - opkg files terminfo should have things like /usr/share/terminfo/x/xterm *not* /mnt/ext/usr/share/terminfo/x/xterm
