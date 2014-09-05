#!/usr/bin/env python

from gi.repository import Gtk
import os
import pickle

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

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

home = os.path.expanduser("~")
conf = os.path.join(home,'.crowbar')

UI_Group = os.path.join('..', 'ui', 'Group.xml')

class Tabs_Manager(grabbo.Notebook):
    def __init__(self, group):
        self.group = group
        super(Tabs_Manager, self).__init__(group.stack)

        if os.path.exists(conf):
            save = pickle.load(open( "session.save", "rb" ))
            for t in save
        else:
            self.add_tab("https://github.com/jeremi360/cRoWBaR")

    def on_add(self, button):
        self.add_tab()

    def add_tab(self, url = None):
        con = Tab(self, url)
        self.add_content(con)

    def add_content(self, content):
        grabbo.Notebook.add_tab(self, content = content.get(), tb = content.tb)
        content.get().show()
        w = self.get_width() + 205
        self.set_width(w)
        self.sc.show()


    def set_width(self, width):
        w = self.group.parent.get_screen().get_width()
        if width < w*0.85:
            self.sc.set_min_content_width(width)

    def get_width(self):
        return self.sc.get_min_content_width()


class Group(grabbo.Builder):
    def __init__(self, parent):
        grabbo.Builder.__init__(self, UI_Group)

        self.stack = Gtk.Stack()

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

    def on_full(self, button):
        self.full.hide()
        self.parent.fullscreen()

    def on_unfull(self, button):
        self.unfull.hide()
        self.parent.unfullscreen()
        self.full.show()

    def set_title(self, title):
        self.parent.hb.set_title("Crowbar: " + title)


class Window(grabbo.Window):
    def __init__(self):
        super(Window, self).__init__()
        self.G = Group(self)

        i = os.path.join(r, 'icons', 'icon.png')
        self.set_icon_from_file(i)

        self.tabs = Tabs_Manager(self.G)

        self.hb = Gtk.HeaderBar()
        self.hb.set_show_close_button(True)
        self.hb.set_title("Crowbar")
        self.hb.set_custom_title(self.tabs.get())
        self.hb.props.border_width = 0
        self.hb.props.margin = 0
        self.hb.pack_start(self.G.StartBox)
        self.hb.pack_end(self.G.EndBox)
        self.hb.set_has_subtitle(False)
        self.set_titlebar(self.hb)

        self.add(self.G.stack)

        self.hb.show()
        self.G.stack.show()
        self.show()

if __name__ == "__main__":
    app = Window()
    Gtk.main()
