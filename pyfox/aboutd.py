import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import grabbo
import pyfox

class AboutD(grabbo.AboutDialog):
    def __init__(self, notebook):
        grabbo.AboutDialog.__init__(self)

        Logo = pyfox.getIcon("icon", "png", 256)
        icon = pyfox.getIcon("icon")
        self.notebook = notebook

        self.set_about_markdown_file(pyfox.aboutFile)
        self.set_appname(pyfox.appName)
        self.set_shortdescrpition(pyfox.comment)
        self.set_version(pyfox.version)
        self.set_license_file(pyfox.licenseText)
        self.get_logo().set_from_pixbuf(Logo)
        self.set_icon(icon)
        self.set_title("About " + pyfox.appName)

        self.add_markdown_file(pyfox.changelog, "ChangeLog")
        self.add_markdown_file(pyfox.toDoFile, "To Do")

        self.show_all()

    def on_home(self, button):
        self.notebook.add_tab(pyfox.home, True)

    def on_report(self, button):
        self.notebook.add_tab(pyfox.rapport, True)

    def on_close(self, button):
        self.close()
