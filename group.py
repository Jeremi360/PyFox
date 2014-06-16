#!/usr/bin/env python

from gi.repository import Gtk
import os
from rerows import Tab, TabButton

UI_Group = os.path.join("ui", "Group.ui")

class Group(object):
    def __init__(self):
        #load UI from UI_FILE
        self.ui = Gtk.Builder()
        self.ui.add_from_file(UI_Group)
        self.ui.connect_signals(self)

        #get objects from UI_FILE
        self.MenuButton = self.ui.get_object("MenuButton")
        self.Add = self.ui.get_object("Add")
        self.Downs = self.ui.get_object("Downs")
        self.Full = self.ui.get_object("Full")
        self.TabsBox = self.ui.get_object("TabsBox")
        self.box = self.ui.get_object("box")

        #add Tabs
        self.Tabs = Gtk.Notebook()
        self.Tabs.set_show_tabs(False)
        self.box.add(self.Tabs)
        self.new_tab()

        self.window.show_all()

    def new_tab(self):
        t = Tab()
        self.Tabs.append_page(t.get())
        b = TabButton(t, self.window)
        self.TabsBox.add(b.get())
        t.get().show()
        b.get().show()

class Window(Gtk.Window):
    def __init__(self):
        self.set_size_request(400, 400)
        self.connect("destroy", Gtk.main_quit)
        G = Group()
        self.add(G)
        self.show()

if __name__ == "__main__":
    app = Window()
    Gtk.main()
