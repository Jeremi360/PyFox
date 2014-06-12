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

        close = self.ui.get_object("close")
        close.connect("clicked", lambda x: self.hide())

        find = self.ui.get_object("find")
        find.connect("activate", lambda x: tab.webview.search_text(tab.find_entry.get_text(), False, True, True))

        prev = self.ui.get_object("back")
        prev.connect("clicked", lambda x: tab.webview.search_text(tab.find_entry.get_text(), False, False, True))

        nextb = self.ui.get_object("nextb")
        nextb.connect("clicked", lambda x: tab.webview.search_text(tab.find_entry.get_text(), False, True, True))


