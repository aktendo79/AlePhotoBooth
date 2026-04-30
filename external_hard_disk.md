<h1>PHOTOS STORED ON AN EXTERNAL HD PLUGGED VIA USB</h1>
Connect the external hard disk (format it exFAT in Windows) and check the address
<pre>lsblk</pre>
Make a dir for mounting point
<pre>sudo mkdir /mnt/PiBooth</pre>
Then mount it
<pre>sudo mount /dev/sda1 /mnt/PiBooth</pre>
Make a directory for the photos
<pre>mkdir -p /media/alessia/PiBooth/Photos</pre>
and give permissions
<pre>sudo chmod -R 777 /media/alessia/PiBooth/Photos</pre>
Now open PiBooth config file
<pre>pibooth --config</pre>
Find this line
<pre># Path to save pictures (list of quoted paths accepted)
directory = ~/Pictures/pibooth</pre>
and change it like this
<pre># Path to save pictures (list of quoted paths accepted)
directory = /media/alessia/PiBooth/Photos</pre>
