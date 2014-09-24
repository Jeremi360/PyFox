from gi.repository import Gtk
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import crowbar
import grabbo

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

Menu_UI = os.path.join(r, 'ui', 'Menu.xml')

class Menu(grabbo.Builder):
    def __init__(self, po, notebook):
        grabbo.Builder.__init__(self, Menu_UI)

        self.notebook = notebook
        self.po = po
        self.Home = self.ui.get_object("Home")
        self.About =  self.ui.get_object("About")
        self.Open = self.ui.get_object("Open")
        self.Save = self.ui.get_object("Save")
        self.Print = self.ui.get_object("Print")
        self.Settings = self.ui.get_object("Settings")
        self.Addons = self.ui.get_object("Addons")
        self.Tools = self.ui.get_object("Tools")
        self.RBug = self.ui.get_object("RaportBug")

        self.Home.connect("clicked", self.on_home)
        self.About.connect("clicked", self.on_about)
        self.RBug.connect("clicked", self.on_rbug)

    def on_home(self, button):
        self.po.hide()
        self.notebook.add_tab(variable.home, True)

    def on_rbug(self, button):
        self.po.hide()
        self.notebook.add_tab(variable.rapport, True)

    def on_about(self, button):
        self.po.hide()
        ad = AboutD(self.notebook)
        ad.run()

    def get(self):
        return self.ui.get_object("grid")

class AboutD(Gtk.AboutDialog):
    def __init__(self, notebook):
        Gtk.AboutDialog.__init__(self)

        img = Gtk.Image()
        img.set_from_file(variable.icon)
        pb = img.get_pixbuf()

        self.set_name(variable.appname)
        self.set_version(variable.version)
        self.set_authors(variable.authors)
        self.set_logo(pb)
        self.set_icon_from_file(variable.icon)
        self.set_comments(variable.comment)
        self.set_license_type(Gtk.License.GPL_3_0)
        self.set_wrap_license(False)
        self.set_title("About " + variable.appname)
        self.set_wrap_license(False)
        self.connect("activate-link", notebook.add_tab)
        self.set_website(variable.home)






