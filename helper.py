
from gi.repository import Gtk

class Window(Gtk.Window):
    def __init__(self, content):
        Gtk.Window.__init__(self)
        self.set_size_request(400, 400)
        self.connect("destroy", Gtk.main_quit)
        self.add(content)
        self.show()

class Group(object):
    def __init__(self):
        #load UI from UI_FILE
        self.ui = Gtk.Builder()
        self.ui.add_from_file(UI_Group)
        self.ui.connect_signals(self)