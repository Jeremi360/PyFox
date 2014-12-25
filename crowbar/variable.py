import os
from gi.repository.GdkPixbuf import Pixbuf

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

appName = "cRoWBaR"
version = "0.07.05"
comment = "Rethinked Web BRowser"
home = "https://github.com/jeremi360/cRoWBaR"
#rapport = "https://github.com/jeremi360/cRoWBaR/issues"
icon = os.path.join(r, 'icons', 'icon.png')
iconSvg = os.path.join(r, 'icons', 'icon.svg')
icon24 = Pixbuf.new_from_file_at_scale(icon, 24, 24, False)
licenseText = os.path.join(r, 'LICENSE')
defaultSearchEngine = "https://duckduckgo.com/?q="
aboutText = "Program and designed by Jeremi 'jeremi360' Biernacki"
tabSize = 384
userDir = os.path.join(os.getenv('HOME'), '.crowbar')
settingsFile = os.path.join(userDir, "settings.pyd")
historyFile = os.path.join(userDir, "history.pyd")
trashFile = os.path.join(userDir, "trash.pyd")
sessionFile = os.path.join(userDir, "session.pyd")
bookmarksFiles = os.path.join(userDir, "bookmarks.pyd")
