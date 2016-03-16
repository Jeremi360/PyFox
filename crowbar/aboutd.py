import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import grabbo
import crowbar

class AboutD(grabbo.AboutDialog):
    def __init__(self, notebook):
        grabbo.AboutDialog.__init__(self)

        Logo = crowbar.getIcon("icon", "png", 256)
        icon = crowbar.getIcon("icon")
        self.notebook = notebook

        self.set_about_markdown_file(crowbar.aboutFile)
        self.set_appname(crowbar.appName)
        self.set_shortdescrpition(crowbar.comment)
        self.set_version(crowbar.version)
        self.set_license_file(crowbar.licenseText)
        self.get_logo().set_from_pixbuf(Logo)
        self.set_icon(icon)
        self.set_title("About " + crowbar.appName)

        self.add_markdown_file(crowbar.changelog, "ChangeLog")
        self.add_markdown_file(crowbar.toDoFile, "To Do")

        self.show_all()

    def on_home(self, button):
        self.notebook.add_tab(crowbar.home, True)

    def on_report(self, button):
        self.notebook.add_tab(crowbar.rapport, True)

    def on_close(self, button):
        self.close()
