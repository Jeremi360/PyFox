#!/usr/bin/env python

from gi.repository import Gtk
import os
from rerows import Tab, TabButton

UI_FILE = os.path.join("ui", "Main.ui")

class Browser(object):
    def __init__(self):
        #load UI from UI_FILE
        self.ui = Gtk.Builder()
        self.ui.add_from_file(UI_FILE)
        self.ui.connect_signals(self)

        #get objects from UI_FILE
        self.MenuButton = self.ui.get_object("MenuButton")
        self.Add = self.ui.get_object("Add")
        self.Downs = self.ui.get_object("Downs")
        self.Full = self.ui.get_object("Full")
        self.TabsBox = self.ui.get_object("TabsBox")
        self.window = self.ui.get_object("Win")
        self.box = self.ui.get_object("box")
        self.window.set_size_request(800, 600)

        #add Tabs
        self.Tabs = Gtk.Notebook()
        self.Tabs.set_show_tabs(False)
        self.box.add(self.Tabs)

        #hide this - don't work yet:
        self.MenuButton.hide()
        self.Downs.hide()
        self.Full.hide()

    def new_tab(self):
        t = Tab()
        self.Tabs.append_page(t.get())
        b = self.TabButton(t)
        self.TabsBox.add(b.get())
        t.get().show()
        b.get().show()



