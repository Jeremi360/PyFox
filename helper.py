
from gi.repository import Gtk
import os

Logo = os.path.join("icons", "logo.svg")

class Window(Gtk.Window):
    def __init__(self, content = Gtk.Box()):
        super(Window, self).__init__()
        self.content = content
        self.do_then_init()
        self.set_size_request(400, 400)
        self.connect("destroy", Gtk.main_quit)
        self.add(self.content)
        self.maximize()
        self.set_icon_from_file(Logo)
        self.show()

    def do_then_init(self):
        pass


class Builder(object):
    def __init__(self, UI_FILE):
        #load UI from UI_FILE
        self.ui = Gtk.Builder()
        self.ui.add_from_file(UI_FILE)
        self.ui.connect_signals(self)