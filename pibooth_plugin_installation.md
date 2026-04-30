pip install pibooth-picture-template
pip install pibooth-sound-effects
pip install pibooth-dropbox
pip install pibooth-qrcode
mkdir /home/<username>/.config/pibooth/CustomPlugins
#-------------------------------------
#use Geany to open:
/home/<username>/.config/pibooth/CustomPlugins/pibooth-neopixel_spi.py
#On another window open to github.com/peteoheat/pibooth-neopixel_spi > 
#Open the file and copy its content in pibooth-neopixel_spi.py
#-------------------------------------
sudo pip3 install adafruit-circuitpython-neopixel-spi
#-------------------------------------
#use Geany to open:
/home/<username>/pibooth/.config/pibooth/pibooth.cfg
#find plugins = and modify as follow:
plugins = CustomPlugins/pibooth_neopixel_spi.py
