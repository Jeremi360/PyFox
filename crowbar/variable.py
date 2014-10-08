import os
from gi.repository.GdkPixbuf import Pixbuf

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

appname = "cRoWBaR"
version = "0.07.04"
comment = "Rethinked Web BRowser"
home = "https://github.com/jeremi360/cRoWBaR"
rapport = "https://github.com/jeremi360/cRoWBaR/issues"
icon = os.path.join(r, 'icons', 'icon.png')
svgicon = os.path.join(r, 'icons', 'icon.svg')
icon24 = Pixbuf.new_from_file_at_scale(icon, 24, 24, False)
licensetxt = os.path.join(r, 'LICENSE')
defaultSearchEngine = "https://duckduckgo.com/?q="
abouttxt = "Program and designed by Jeremi 'jeremi360' Biernacki"
tabsize = 384
userdir = os.path.join(os.getenv('HOME'), '.crowbar')
settingsFile = os.path.join(userdir, "settings.pyd")
historyFile = os.path.join(userdir, "history.pyd")
trashFile = os.path.join(userdir, "trash.pyd")
sessionFile = os.path.join(userdir, "session.pyd")
