from gi.repository import Gtk
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import crowbar
import grabbo

UI_Main = os.path.join(crowbar.appdir, 'ui', 'Main.xml')
class MainControls(grabbo.Builder):
    def __init__(self, parent):
        grabbo.Builder.__init__(self, UI_Main)

        self.notebook = None
        self.parent = parent
        self.menub = self.ui.get_object("MenuButton")
        self.downs = self.ui.get_object("Downs")
        self.EndBox = self.ui.get_object("EndBox")

        self.menub.connect("clicked", self.on_menu)

    def set_title(self, title):
        self.parent.hb.set_title(crowbar.appname + ": " + title)

    def on_menu(self, button):
        po = Gtk.Popover.new(self.menub)
        m = crowbar.Menu(po, self.notebook).get()
        po.add(m)
        po.show()
