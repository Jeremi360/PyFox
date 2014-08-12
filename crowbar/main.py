#!/usr/bin/env python

from gi.repository import Gtk
from crowbar.tab import Tab
import grabbo
import os

UI_Group = os.path.join('..', 'ui', 'Group.ui')

class Tabs(grabbo.Notebook):
    def __init__(self, paronama):
        super(Tabs, self).__init__()
        self.paronama = paronama

        self.add_tab("https://github.com/jeremi360/cRoWBaR")

        self.buttons_box.show()
        self.pages.show()

    def add_tab(self, url = None):
        bt = grabbo.TabButton()
        bt.set(self, 0, "New Tab", True)
        content = Tab(bt, url, self.paronama).get()
        super(Tabs, self).add_tab(content, bt)

class Group(grabbo.Builder):
    def __init__(self, parent):
        grabbo.Builder.__init__(self, UI_Group)

        self.parent = parent
        #get objects from UI_FILE
        self.menub = self.ui.get_object("MenuButton")
        self.downs = self.ui.get_object("Downs")
        self.full = self.ui.get_object("Full")
        self.unfull = self.ui.get_object("UnFull")
        self.box = self.ui.get_object("MainBox")

        self.unfull.hide()

        self.full.connect("clicked", self.on_full)
        self.unfull.connect("clicked", self.on_unfull)

        #add Tabs
        self.tabs = Tabs(self)
        self.box.add(self.tabs.get())
        self.tabs.get().show()
        self.parent.add(self.tabs.pages)
        self.box.show()

    def set_title(self, text):
        self.parent.set_name(text)

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
        G = Group(self).box
        G.show()

        hb = Gtk.HeaderBar()
        hb.props.show_close_button = True
        hb.props.title = ""
        hb.add(G)
        G.set_vexpand(True)
        G.set_vexpand_set(True)
        self.set_titlebar(hb)
        hb.show()

        self.add(G)
        self.show()

if __name__ == "__main__":
    app = Window()
    Gtk.main()
