
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
        super(Window, self).__init__(UI_WC)
        self.wc = self.ui.get_object("box")
        self.content = content
        self.do_then_init()

        if wc_box == None:
            try:
                self.content.end_pack(self.wc, False, False, False, 0)


        self.set_size_request(400, 400)
        self.connect("destroy", Gtk.main_quit)
        self.add(self.content)
        self.maximize()
        self.set_icon_from_file(Logo)
        self.show()

    def do_then_init(self):
        pass

