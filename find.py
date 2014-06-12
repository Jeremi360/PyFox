# forked from https://gist.github.com/kklimonda/890640
# by Jeremi "jeremi360" Biernacki

from gi.repository import Gtk
import os

UI_find = os.path.join("ui", "Find.ui")

class Find(Gtk.ButtonBox):
    def __init__(self, tab):
        self.ui = Gtk.Builder()
        self.ui.add_from_file(UI_find)
        self.ui.connect_signals(self)

        close_button = self.ui.get_object("Fclose")
        close_button.connect("clicked", lambda x: self.hide())

        self.find_entry = self.ui.get_object("Fentry")
        self.find_entry.connect("activate", lambda x: tab.webview.search_text(tab.find_entry.get_text(), False, True, True))

        prev_button = self.ui.get_object("Fback")
        prev_button.connect("clicked", lambda x: tab.webview.search_text(tab.find_entry.get_text(), False, False, True))

        next_button = self.ui.get_object("Fnext")
        next_button.connect("clicked", lambda x: tab.webview.search_text(tab.find_entry.get_text(), False, True, True))


