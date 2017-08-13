#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pyfox, grabbo

class Main(grabbo.Window):
    def __init__(self):
        grabbo.Window.__init__(self)

        if not os.path.exists(pyfox.userDir):
            os.mkdir(pyfox.userDir)

        if not os.path.exists(pyfox.bookmarksFiles):
            pyfox.savePydFile(pyfox.bookmarksFiles, [])

        if not os.path.exists(pyfox.historyFile):
            pyfox.savePydFile(pyfox.historyFile, [])

        if not os.path.exists(pyfox.sessionFile):
            pyfox.savePydFile(pyfox.sessionFile, [])

        if not os.path.exists(pyfox.settingsFile):
            pyfox.savePydFile(pyfox.settingsFile, {})

        if not os.path.exists(pyfox.trashFile):
            pyfox.savePydFile(pyfox.trashFile, [])

        self.hb = Gtk.HeaderBar()
        self.MC = pyfox.MainControls(self)
        self.set_icon(pyfox.getIcon('icon'))

        self.tabs = pyfox.TabControls(self.MC)
        self.MC.notebook = self.tabs.notebook
        self.tabs.notebook.add_tab(url=pyfox.home, active=True)

        self.hb.set_show_close_button(True)
        self.hb.set_title(pyfox.appName)
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
