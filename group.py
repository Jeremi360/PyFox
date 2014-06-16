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
        self.menub = self.ui.get_object("MenuButton")
        self.add = self.ui.get_object("Add")
        self.downs = self.ui.get_object("Downs")
        self.full = self.ui.get_object("Full")
        self.box = self.ui.get_object("TabsBox")

        #add Tabs
        self.tabs = Gtk.Notebook()
        self.tabs.set_show_tabs(False)
        self.new_tab()
        self.get().pack_start(self.Tabs, True, True, 0)
        self.tabs.show()
        self.get().show()

    def set_title(self, text):
        self.parent.set_title(text)

    def get(self):
        return self.ui.get_object("box")

    def new_tab(self):
        t = Tab(self.parent)
        self.tabs.append_page(t.get())
        self.box.add(t.button.get())
        old = self.get().child_get_property(self.add, "position")
        self.get().reorder_child(self.add, old + 1)

class Window(helper.Window):
    def __init__(self):
        super(Window, self).__init__()

    def do_then_init(self):
        self.content = Group(self).get()

if __name__ == "__main__":
    app = Window()
    Gtk.main()
