# forked from https://gist.github.com/kklimonda/890640
# by Jeremi "jeremi360" Biernacki

from gi.repository import Gtk
import os

UI_find = os.path.join("ui", "Find.ui")

class Find(object):
    def __init__(self, tab):
        self.ui = Gtk.Builder()
        self.ui.add_from_file(UI_find)
        self.ui.connect_signals(self)




