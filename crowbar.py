#!/usr/bin/env python

from gi.repository import Gtk
from tab import Tab
import grabbo
import os

UI_Group = os.path.join("ui", "Group.ui")

class Group(grabbo.Builder):
    def __init__(self, parent):
        grabbo.Builder.__init__(self, UI_Group)

        self.parent = parent
        #get objects from UI_FILE
        self.menub = self.ui.get_object("MenuButton")
        self.add = self.ui.get_object("Add")
        self.downs = self.ui.get_object("Downs")
        self.full = self.ui.get_object("Full")
        self.unfull = self.ui.get_object("UnFull")
        self.box = self.ui.get_object("MainBox")

        self.unfull.hide()

        self.add.connect("clicked", lambda x: self.new_tab())
        self.full.connect("clicked", self.on_full)
        self.unfull.connect("clicked", self.on_unfull)

        #add Tabs
        self.notebook = grabbo.Notebook(content = {Tab(self):"New Tab"}, addable_content = (Tab(self), "New Tab"))
        self.get().pack_start(self.notebook.pages, True, True, 0)
        self.
        self.notebook.show()
        self.get().show()

    def set_title(self, text):
        self.parent.set_title(text)

    def get(self):
        return self.ui.get_object("box")

    def on_full(self, button, name):
        self.full.hide()
        self.parent.fullscreen()
        self.unfull.show()

    def on_unfull(self, button, name):
        self.unfull.hide()
        self.parent.unfullscreen()
        self.full.show()

class Window(grabbo.Window):
    def __init__(self):
        super(Window, self).__init__()
        G = Group(self).get()
        G.show()
        self.add(G)
        self.show()

if __name__ == "__main__":
    app = Window()
    Gtk.main()
