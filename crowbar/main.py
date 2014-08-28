#!/usr/bin/env python

from gi.repository import Gtk
import os

try:
    from crowbar.tab import Tab
    print("Eclipse way")
except:
    from tab import Tab
    print("Normal way")

try:
    import grabbo
except:
    print("Please first install Grabbo in your python path or copy to crowbar dir")
    print("Grabbo can be download from https://github.com/jeremi360/Grabbo")
    exit()


UI_Group = os.path.join('..', 'ui', 'Group.ui')

class Tabs_Manager(grabbo.Notebook):
    def __init__(self, group):
        super(Tabs_Manager, self).__init__()
        group.StartBox.pack_end(self.ButtonBox, True, True, True)

        self.AddButton_tab("https://github.com/jeremi360/cRoWBaR")

    def AddButton_tab(self, url = None):
        con = Tab(url)
        super(Tabs_Manager, self).AddButton_tab(con.get(), "New tab")


class Group(grabbo.Builder):
    def __init__(self, parent):
        grabbo.Builder.__init__(self, UI_Group)

        self.parent = parent
        self.menub = self.ui.get_object("MenuButton")
        self.downs = self.ui.get_object("Downs")
        self.full = self.ui.get_object("Full")
        self.unfull = self.ui.get_object("UnFull")
        self.StartBox = self.ui.get_object("StartBox")
        self.EndBox = self.ui.get_object("EndBox")

        self.unfull.hide()
        self.full.hide()

        #self.full.connect("clicked", self.on_full)
        #self.unfull.connect("clicked", self.on_unfull)

        self.StartBox.show()
        self.EndBox.show()

    def on_full(self, button):
        self.full.hide()
        self.parent.fullscreen()

    def on_unfull(self, button):
        self.unfull.hide()
        self.parent.unfullscreen()
        self.full.show()

    def set_width(self, width):
        width = width*0.8
        self._scroll.set_min_content_width(width)

class Window(grabbo.Window):
    def __init__(self):
        super(Window, self).__init__()
        self.G = Group(self)

        self.tabs = Tabs_Manager(self.G)

        self.modern()
        #self.old()

        self.show()

    def modern(self):
        w = self.get_screen().get_width()
        print(w)
        #self.G.set_width(w)
        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.set_title("")
        hb.set_custom_title(Gtk.Separator())
        hb.props.border_width = 0
        hb.props.margin = 0
        hb.pack_start(self.G.StartBox)
        hb.pack_end(self.G.EndBox)
        hb.set_has_subtitle(False)
        self.set_titlebar(hb)
        self.tabs.switcher.show()
        self.tabs.AddButton.show()
        hb.show()

        self.add(self.tabs.stack)
        self.tabs.stack.show()

    def old(self):
        box = Gtk.Box()
        box.set_orientation(Gtk.Orientation.HORIZONTAL)
        box.pack_start(self.G.StartBox, True, True, True)
        box.pack_start(self.G.EndBox, False, True, True)
        box.show()

        box_zwei = Gtk.Box()
        box_zwei.set_orientation(Gtk.Orientation.VERTICAL)
        box_zwei.pack_start(box, False, True, True)
        box_zwei.pack_end(self.tabs.pages, True, True, True)
        box_zwei.show()

        self.add(box_zwei)

if __name__ == "__main__":
    app = Window()
    Gtk.main()
