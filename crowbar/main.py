#!/usr/bin/env python3

from gi.repository import Gtk
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import crowbar
import grabbo

class Main(grabbo.Window):
    def __init__(self):
        grabbo.Window.__init__(self)

        if not os.path.exists(crowbar.userDir):
            os.mkdir(crowbar.userDir)

        if not os.path.exists(crowbar.trashFile):
            crowbar.SaveTrash([])





        self.hb = Gtk.HeaderBar()
        self.MC = crowbar.MainControls(self)
        self.set_icon_from_file(crowbar.icon)

        self.tabs = crowbar.TabControls(self.MC)
        self.MC.notebook = self.tabs.notebook
        self.tabs.notebook.add_tab(url = crowbar.home, active = True)

        self.hb.set_show_close_button(True)
        self.hb.set_title(crowbar.appName)
        self.hb.props.border_width = 0
        self.hb.props.margin = 0
        self.hb.pack_start(self.MC.menub)
        self.hb.set_custom_title(self.MC.TitleBox)
        self.hb.pack_end(self.MC.EndBox)
        self.hb.set_has_subtitle(False)
        self.set_titlebar(self.hb)

        self.add(self.tabs.get())

        self.maximize()

        self.hb.show()
        self.tabs.get().show()
        self.show()

    def on_close(self, button):
        grabbo.Window.on_close(self, button)

if __name__ == "__main__":
    app = Main()
    Gtk.main()
