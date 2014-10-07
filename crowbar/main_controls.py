from gi.repository import Gtk
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import crowbar
import grabbo

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

UI_Main = os.path.join(r, 'ui', 'MainControls.xml')
class MainControls(grabbo.Builder):
    def __init__(self, parent):
        grabbo.Builder.__init__(self, UI_Main)

        self.notebook = None
        self.parent = parent
        self.menub = self.ui.get_object("MenuButton")
        self.downs = self.ui.get_object("Downs")
        self.EndBox = self.ui.get_object("EndBox")
        self.TitleBox = self.ui.get_object("TitleBox")
        self.Title = self.ui.get_object("Title")
        self.TBox = self.ui.get_object("Tbox")
        self.Icon = self.ui.get_object("Icon")
        self.sc = self.ui.get_object("scrolledwindow")
        self.addb = self.ui.get_object("AddButton")
        self.TabsSwitcher = self.ui.get_object("TabsSwitcher")

        self.menub.get_image().set_from_pixbuf(crowbar.icon24)
        self.menub.connect("clicked", self.on_menu)

        self.set_title()
        self.auto_set_TabSwitcher_width()
        self.sc.hide()

    def set_title(self, title = None):
        if title is None:
            t = crowbar.appname
        else:
            t = crowbar.appname + ": " + title

        self.parent.hb.set_title(t)
        self.Title.set_label(t)

    def auto_set_TabSwitcher_width(self):
        maxw = self.parent.get_allocation().width*0.85
        neww = self.TabsSwitcher.get_allocation().width
        minw = crowbar.tabsize

        if neww <= maxw:
            if neww >= minw:
                self.sc.set_min_content_width(neww)
            else:
                self.sc.set_min_content_width(minw)
        else:
            self.sc.set_min_content_width(maxw)

    def on_menu(self, button):
        po = Gtk.Popover.new(self.menub)
        m = crowbar.Menu(po, self.notebook).get()
        po.add(m)
        po.show()
