from crowbar.extension import Extension
from gi.repository import Gtk

Name = "ToTop"
shortDes = "Go To Top of page",
Descrption = "and nothing more :P",
Author = "Jeremi 'jeremi360' Biernacki"
url_1 = "https://github.com/jeremi360/cRoWBaR"
url_2 = "/blob/master/crowbar/extensions/totop.py"
url = "".join(url_1, url_2)
Icon = Gtk.STOCK_GOTO_TOP

class ToTop(Extension):
    def __init__(self):
        super(ToTop, self).__init__(
                                    Crowbar,
                                    Name, shortDes,
                                    Descrption, Author,
                                    url, Icon
                                    )


