from gi.repository import Gtk, WebKit
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import crowbar
import grabbo

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

TabB_UI = os.path.join(r, "ui", "TabButton.xml")
class TabButton (grabbo.Builder):
    def __init__(self, notebook):
        grabbo.Builder.__init__(self, TabB_UI)
        self.TabB = self.ui.get_object("TabbButton")
        self.removeB = self.ui.get_object("RemoveButton")

        self.num = 0
        self.notebook = notebook

        self.TabB.connect("toggled", self.on_tab)

    def set_num(self, num):
        self.num = num

    def get(self):
        return self.ui.get_object("box")

    def on_tab(self, button):
        self.notebook.set_current_page(self.num)

    def on_remove(self, button):
        self.notebook.remove_page(self.num)

class SwVpWv(Gtk.ScrolledWindow):
    def __init__(self, url):
        Gtk.ScrolledWindow.__init__(self)
        self.webview = WebKit.WebView()
        self.add(self.webview)
        self.webview.load_uri(url)
        self.show_all()

class Notebook(Gtk.Notebook):
    def __init__(self, tabcontrols):
        Gtk.Notebook.__init__(self)
        self.tabc = tabcontrols
        self.get_show_tabs(False)



