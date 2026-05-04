<h1>RaspbianOS first configuration</h1>
<pre>
sudo apt-get update
sudo apt-get full-upgrade
sudo apt-get install libsdl2-*
sudo apt-get install cups libcups2-dev
sudo usermod -a -G lpadmin <username>
sudo pip3 install pibooth[printer]
sudo apt-get install python3-opencv
</pre>
#-------------------------------------
<pre>sudo nano /boot/config.txt</pre>
at the very bottom add
<pre>dtoverlay=gpio-shutdown</pre>
#-------------------------------------
<pre>sudo nano /etc/cups/cupsd.conf</pre>
disable the line Listen localhost:631 and add
<pre>Port 631</pre>
find Restrict access to the server... and modify as follow
<pre>
< Location />
  Order allow,deny
  Allow @local
< /Location>
</pre>
find Restrict access to the admin pages... and modify as follow
<pre>
< Location /admin>
  Order allow,deny
  Allow @local
< /Location>
</pre>
find Restrict access to configuration files... and modify as follow
<pre>
< Location /admin/conf>
  AuthType Default
  Require user @SYSTEM
  Order allow,deny
  Allow @local
< /Location>
</pre>
#-------------------------------------
<pre>/etc/init.d/cups restart</pre>
authenticate when required<br>
#-------------------------------------
<pre>sudo raspi-config</pre>
Interface Options > Legacy camera enabled > Ok > Finish > Yes reboot<br>
#-------------------------------------
<pre>sudo nano /boot/config.txt</pre>
go to the bottom and add
<pre>hdmi_cvt=1024 600 60 3 0 0 0</pre>
#-------------------------------------
<pre>sudo raspi-config</pre>
Performance Options > GPU Memory > 192 > Ok > Finish > Yes reboot<br>
#-------------------------------------
