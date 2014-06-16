
from gi.repository import Gtk

class Window(Gtk.Window):
    def __init__(self, content):
        super(Window, self).__init__()
        self.set_size_request(400, 400)
        self.connect("destroy", Gtk.main_quit)
        self.add(content)
        self.show()


class Builder(object):
    def __init__(self, UI_FILE):
        #load UI from UI_FILE
        self.ui = Gtk.Builder()
        self.ui.add_from_file(UI_FILE)
        self.ui.connect_signals(self)