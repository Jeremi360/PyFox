
from gi.repository import Gtk
import os

Logo = os.path.join("icons", "logo.svg")


class Builder(object):
    def __init__(self, UI_FILE):
        #load UI from UI_FILE
        self.ui = Gtk.Builder()
        self.ui.add_from_file(UI_FILE)
        self.ui.connect_signals(self)

UI_WC = os.path.join("ui", "WindowControls.ui")

class Window(Builder, Gtk.Window):
    def __init__(self, content = Gtk.Box(), wc_box = None):
        Gtk.Window.__init__(self)
        Builder.__init__(self, UI_WC)

        self.wc = self.ui.get_object("box")
        self.content = content
        self.do_then_init()

        if wc_box == None:
            try:
                self.add_wc(self.content)
            except:
                self.connect("destroy", Gtk.main_quit())
        else:
            self.add_wc(wc_box)

        self.set_size_request(400, 400)
        self.add(self.content)
        self.maximize()
        self.set_icon_from_file(Logo)
        self.show()

    def mac(self):
        try:
            self.maximize()
        except:
            self.unmaximize()

    def add_wc(self, wc_box):
        close = self.ui.get_object("close")
        close.connect("clicked", Gtk.main_quit())

        maks = self.ui.get_object("max")
        maks.connect("clicked", self.mac())

        mini = self.ui.get_object("mini")
        mini.connect("clicked", self.iconify())

        self.set_decorated(False)
        wc_box.end_pack(self.wc, False, False, 0)
        self.wc.show()

    def do_then_init(self):
        pass

if __name__ == "__main__":
    app = Window()
    Gtk.main()