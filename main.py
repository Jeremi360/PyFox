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

        self.tabs = []

        #get objects from UI_FILE
        self.Tabs = self.ui.get_object("tabs")
        self.MenuButton = self.ui.get_object("MenuButton")
        self.Add = self.ui.get_object("Add")
        self.Downs = self.ui.get_object("Downs")
        self.Full = self.ui.get_object("Full")
        self.TabsBox = self.ui.get_object("TabsBox")
        self.window = self.ui.get_object("window")

        self.window.set_size_request(800, 600)

        #hide this - don't work yet:
        self.MenuButton.hide()
        self.Downs.hide()
        self.Full.hide()


    def new_tab(self):
        view = Tab().box
        self.TabsBox.gtk_container_add(self.TabButton().get())
        self.Tabs.

