from gi.repository import Gtk
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from crowbar import variable

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
        self.connect("activate-link", notebook.add_tab())
        self.set_website(variable.home)
