import os, sys
import grabbo
import crowbar
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

class AboutD(grabbo.AboutDialog):
    def __init__(self, notebook):
        grabbo.AboutDialog.__init__(self)
        self.notebook = notebook
        self.set_about_text(crowbar.aboutText)
        self.set_appname(crowbar.appName)
        self.set_shortdescrpition(crowbar.comment)
        self.set_version(crowbar.version)
        self.set_license_text_file(crowbar.licenseText)
        self.Logo.set_from_pixbuf(crowbar.getIcon("icon", "png", 256))
        self.set_icon(crowbar.getIcon("icon"))
        self.set_title("About " + crowbar.appName)
        
        self.preshow()

    def on_home(self, button):
        self.notebook.add_tab(crowbar.home, True)
        
    def on_rapport(self, button):
        self.notebook.add_tab(crowbar.rapport, True)


