#!/usr/bin/env python

from gi.repository import Gtk
import os
from rerows import Tab, TabButton
import helper

UI_Group = os.path.join("ui", "Group.ui")

class Group(helper.Builder):
    def __init__(self, parent):
        super(Group, self).__init__(UI_Group)
        self.parent = parent

        #get objects from UI_FILE
        self.MenuButton = self.ui.get_object("MenuButton")
        self.Add = self.ui.get_object("Add")
        self.Downs = self.ui.get_object("Downs")
        self.Full = self.ui.get_object("Full")
        self.TabsBox = self.ui.get_object("TabsBox")

        #add Tabs
        self.Tabs = Gtk.Notebook()
        self.Tabs.set_show_tabs(False)
        self.new_tab()
        self.get().pack_start(self.Tabs, True, True, 0)

        self.get().show()

    def set_title(self, text):
        self.parent.set_title(text)

    def get(self):
        return self.ui.get_object("box")

    def new_tab(self):
        t = Tab(self.parent)
        self.Tabs.append_page(t.get())
        self.TabsBox.add(t.button.get())
        self.get().reorder_child(self.Add, -1)

class Window(helper.Window):
    def __init__(self):
        super(Window, self).__init__()

    def do_then_init(self):
        self.content = Group(self).get()

if __name__ == "__main__":
    app = Window()
    Gtk.main()
