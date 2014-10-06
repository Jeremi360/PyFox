from gi.repository import Gtk
import os, sys
import grabbo
import crowbar
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

class AboutD(grabbo.AboutDialog):
    def __init__(self, notebook):
        grabbo.AboutDialog.__init__(self)
        self.set_about_text(crowbar.abouttxt)
        self.set_appname(crowbar.appname)
        self.set_shortdescrpition(crowbar.comment)
        self.set_home_page(crowbar.home)
        self.set_rapport_page(crowbar.rapport)

