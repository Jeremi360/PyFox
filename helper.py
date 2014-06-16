
from gi.repository import Gtk

class Window(Gtk.Window):
    def __init__(self, content):
        Gtk.Window.__init__(self)
        self.set_size_request(400, 400)
        self.connect("destroy", Gtk.main_quit)
        self.add(content)
        self.show()
