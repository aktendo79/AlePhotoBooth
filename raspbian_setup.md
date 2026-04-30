sudo apt-get update
sudo apt-get full-upgrade
sudo apt-get install libsdl2-*
sudo apt-get install cups libcups2-dev
sudo usermod -a -G lpadmin <username>
sudo pip3 install pibooth[printer]
sudo apt-get install python3-opencv
#-------------------------------------
sudo nano /boot/config.txt
#at the very bottom add
dtoverlay=gpio-shutdown
#-------------------------------------
sudo nano /etc/cups/cupsd.conf
#disable the line Listen localhost:631 and add
Port 631
#find Restrict access to the server... and modify as follow
<Location />
  Order allow,deny
  Allow @local
</Location>
#find Restrict access to the admin pages... and modify as follow
<Location /admin>
  Order allow,deny
  Allow @local
</Location>
#find Restrict access to configuration files... and modify as follow
<Location /admin/conf>
  AuthType Default
  Require user @SYSTEM
  Order allow,deny
  Allow @local
</Location>
#-------------------------------------
/etc/init.d/cups restart
#authenticate when required
#-------------------------------------
sudo raspi-config
#Interface Options > Legacy camera enabled > Ok > Finish > Yes reboot
#-------------------------------------
sudo nano /boot/config.txt
#go to the bottom and add
hdmi_cvt=1024 600 60 3 0 0 0
#-------------------------------------
sudo raspi-config
#Performance Options > GPU Memory > 192 > Ok > Finish > Yes reboot
#-------------------------------------
