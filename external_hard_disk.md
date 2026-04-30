#---PHOTOS STORED ON AN EXTERNAL HD PLUGGED VIA USB---
#---Connect the external hard disk (format it exFAT in Windows) and check the address---
lsblk
#---Make a dir for mounting point---
sudo mkdir /mnt/PiBooth
#---Then mount it---
sudo mount /dev/sda1 /mnt/PiBooth
#---Make a directory for the photos---
mkdir -p /media/alessia/PiBooth/Photos
#---and give permissions---
sudo chmod -R 777 /media/alessia/PiBooth/Photos
#---Now open PiBooth config file---
pibooth --config
#---Find this line---
# Path to save pictures (list of quoted paths accepted)
directory = ~/Pictures/pibooth
#---and change it like this---
# Path to save pictures (list of quoted paths accepted)
directory = /media/alessia/PiBooth/Photos
