from crowbar.extension import Extension
from crowbar.tab import Tab
from gi.repository import Gtk

Name = "ToTop"
shortDes = "Go To Top of page",
Descrption = "and nothing more :P",
Author = "Jeremi 'jeremi360' Biernacki"
url_1 = "https://github.com/jeremi360/cRoWBaR"
url_2 = "/blob/master/crowbar/extensions/totop.py"
url = "".join(url_1, url_2)
Icon = Gtk.STOCK_GOTO_TOP

class _Button(Gtk.Button):
    def __init__(self, ui):
        self._ui = ui.scroll
        self.set_image(Icon)
        self.connect("clicked", lambda x: self.on_bu)

    def on_bu(self):
        self._ui.do_scroll_child(
                                 self.ui.scroll,
                                 Gtk.ScrollType.START,
                                 False
                                 )



class ToTop(Extension):
    def __init__(self, UI):
        super(ToTop, self).__init__(
                                    UI, Name, shortDes,
                                    Descrption, Author,
                                    url, Icon
                                    )

    def work(self):
        self._bu = _Button(self.)






