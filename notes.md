#PirateBox Notes

Installed newest openwrt trunk snapshot (11/Feb/2012)
Change LAN interface to be home LAN ip range (static 192.168.0.111)
Wireless doesn't seem to be present (not enabled?)

Alter /etc/fstab so that usb mounted filesystem is type ext4 eg: change lines in /etc/fstab:

	/dev/sda1       /mnt/usb        vfat    rw,sync,umask=0 0       0
	to
	/dev/sda1       /mnt/usb        ext4    rw,sync,umask=0 0       0
	
Power off

Copy files from vfat created usb drive. Reformat drive as ext4, place files back on usb, startup...

##Packages added

add these two lines to /etc/profile to allow library paths etc.
	
	export LD_LIBRARY_PATH=/lib:/usr/lib:/usr/local/lib 
	export PATH=$PATH:/mnt/ext/usr/sbin:/mnt/ext/usr/bin

Install with:

	opkg install <pkg>

###shadow-useradd

Use to add a non privileged user [useradd xxx]

Need to set home dir in passwd file to something like /mnt/usb/home/xxx
Set ownership of this directory to user xxx

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
