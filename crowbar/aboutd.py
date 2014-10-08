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
        self.set_home_page(crowbar.home)
        self.set_rapport_page(crowbar.rapport)
        self.set_version(crowbar.version)
        self.set_license_custom(crowbar.licenseText)
        self.set_logo_from_file(crowbar.icon)
        self.set_title("About " + crowbar.appName)

    def open_link(self, url):
        self.notebook.add_tab(url, True)


