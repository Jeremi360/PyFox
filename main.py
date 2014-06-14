#!/usr/bin/env python

from gi.repository import Gtk
import os
from rerows import Tab

UI_FILE = os.path.join("ui", "Main.ui")

class Browser(object):
    def __init__(self):
        #load UI from UI_FILE
        self.ui = Gtk.Builder()
        self.ui.add_from_file(UI_FILE)
        self.ui.connect_signals(self)

