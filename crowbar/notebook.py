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
        self.Label = self.ui.get_object("label")
        self.Icon = self.ui.get_object("icon")
        self.Button = self.ui.get_object("button")
        self.num = 0
        self.notebook = notebook

        self.Button.connect("clicked", self.on_button)

    def set_num(self, num):
        self.num = num

    def get(self):
        return self.ui.get_object("box")

    def on_button(self, button):
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
        self.set_scrollable(True)
        self.tabc = tabcontrols






