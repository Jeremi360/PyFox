from crowbar.extension import Extension
from gi.repository import Gtk

Name = "ToTop"
shortDes = "Go To Top of page",
Descrption = "and nothing more :P",
Author = "Jeremi 'jeremi360' Biernacki"
url = ""
Icon = Gtk.STOCK_GOTO_TOP

class ToTop(Extension):
    def __init__(self):
        super(ToTop, self).__init__(
                                    Name, shortDes,
                                    Descrption, Author,
                                    url, Icon
                                    )
