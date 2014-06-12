from gi.repository import Gtk, GdkPixbuf, WebKit
import os, sys

class Find(Gtk.HBox):
    def __init__(self, tab):
        close_button = Gtk.Button("Close")
        close_button.connect("clicked", lambda x: self.hide())
        self.find_entry = Gtk.Entry()
        self.find_entry.connect("activate",
                                lambda x: tab.webview.search_text(tab.find_entry.get_text(),
                                                                   False, True, True))
        prev_button = Gtk.Button("Previous")
        next_button = Gtk.Button("Next")
        prev_button.connect("clicked",
                            lambda x: tab.webview.search_text(tab.find_entry.get_text(),
                                                               False, False, True))
        next_button.connect("clicked",
                            lambda x: tab.webview.search_text(tab.find_entry.get_text(),
                                                               False, True, True))

        self.pack_start(url_box, False, False, 0)
        self.pack_start(scrolled_window, True, True, 0)
        self.pack_start(find_box, False, False, 0)

