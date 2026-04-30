pibooth
#-------------------------------------
#when it opens press ESC and the menu appears
#General > Manage Plugins
#Window > Startup size = fullscreen > Wait picture display time = 60
#Picture > Orientation = auto > Title = Footer 1 > Sub-title = Footer 2
#Printer > Maximum of printed duplicates = 1
#
#
#-------------------------------------
#use Geany to open:
/home/<username>/pibooth/.config/pibooth/pibooth.cfg
#find footer_text2 = Footer 2 and modify as follow:
footer_text2 = "{date.day}/{date.month}/{date.year}"
#find resolution = (1934, 2464) and modify as follow:
resolution = (3280, 2464)
#find debounce_delay = 0.3 and modify as follow:
debounce_delay = 0.1
#find prefix_url = https://github.com/pibooth/pibooth and modify as follow:
prefix_url = {url}
#find side_text = and modify as follow:
side_text = "Download Pic!"
#find wait_location = bottomleft and modify as follow:
wait_location = topleft
#find print_location = bottomleft and modify as follow:
print_location = topright
#find album_name = and modify as follow:
album_name = Pibooth
#find app_key = and modify as follow:
app_key =
#find app_secret = and modify as follow:
app_secret =
#find template = picture_template.xml and modify as follow:
template = picture_template2.xml
#-------------------------------------
