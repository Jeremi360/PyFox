from gi.repository import Gtk
import os

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

import crowbar
import grabbo

UI_Main = os.path.join(r, 'ui', 'Main.xml')
class Main_Controls(grabbo.Builder):
    def __init__(self, parent):
        grabbo.Builder.__init__(self, UI_Main)

        self.notebook = None
        self.parent = parent
        self.menub = self.ui.get_object("MenuButton")
        self.downs = self.ui.get_object("Downs")
        self.StartBox = self.ui.get_object("StartBox")
        self.EndBox = self.ui.get_object("EndBox")

        self.menub.connect("clicked", self.on_menu)

    def set_title(self, title):
        self.parent.hb.set_title(variable.appname + ": " + title)

    def on_menu(self, button):
        po = Gtk.Popover.new(self.menub)
        m = Menu(po, self.notebook).get()
        po.add(m)
        po.show()
