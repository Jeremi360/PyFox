from gi.repository import Gtk, GdkPixbuf, WebKit
import os, sys

UI_find = os.path.join("ui", "Find.ui")

class Find(Gtk.HBox):
    def __init__(self, tab):
        self.ui = Gtk.Builder()
        self.ui.add_from_file(UI_find)
        self.ui.connect_signals(self)

        close_button = self.ui.get_object("Fclose")
        close_button.connect("clicked", lambda x: self.hide())

        self.find_entry = self.ui.get_object("Fentry")
        self.find_entry.connect("activate",
                                lambda x: tab.webview.search_text(tab.find_entry.get_text(),
                                False, True, True))

        prev_button = self.ui.get_object("Fback")
        prev_button.connect("clicked",
                            lambda x: tab.webview.search_text(tab.find_entry.get_text(),
                            False, False, True))

        next_button = self.get_object("Fnext")
        next_button.connect("clicked",
                            lambda x: tab.webview.search_text(tab.find_entry.get_text(),
                            False, True, True))

        self.pack_start(url_box, False, False, 0)
        self.pack_start(scrolled_window, True, True, 0)
        self.pack_start(find_box, False, False, 0)

