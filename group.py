#!/usr/bin/env python

from gi.repository import Gtk
import os
from rerows import Tab, TabButton
import helper

UI_Group = os.path.join("ui", "Group.ui")

class Group(helper.Builder):
    def __init__(self, window):
        super(Group, self).__init__(UI_Group)
        self.window = window

        #get objects from UI_FILE
        self.MenuButton = self.ui.get_object("MenuButton")
        self.Add = self.ui.get_object("Add")
        self.Downs = self.ui.get_object("Downs")
        self.Full = self.ui.get_object("Full")
        self.TabsBox = self.ui.get_object("TabsBox")

        #add Tabs
        self.Tabs = Gtk.Notebook()
        self.Tabs.set_show_tabs(False)
        self.get().add(self.Tabs)
        self.new_tab()

        self.get().show()

    def get(self):
        return self.ui.get_object("box")

    def new_tab(self):
        b = TabButton(t, self.window)
        t = Tab(b, self.window)
        self.Tabs.append_page(t.get())
        self.TabsBox.add(b.get())
        t.get().show()
        b.get().show()

class Window(helper.Window):
    def __init__(self):
        T = Group(self)
        super(Window, self).__init__(T)

if __name__ == "__main__":
    app = Window()
    Gtk.main()
