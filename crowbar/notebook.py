from gi.repository import Gtk, WebKit
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import crowbar
import grabbo

TabL_UI = os.path.join(crowbar.get_appdir(), "ui", "TabLabel.xml")
class TabLabel (grabbo.Builder):
    def __init__(self, notebook):
        grabbo.Builder.__init__(self, TabL_UI)
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


class Notebook(Gtk.Notebook):
    def __init__(self):
        Gtk.Notebook.__init__(self)
        self.set_scrollable(True)

    def append_page(self, url = None):
        tl = TabLabel(self)
        sc = Gtk.ScrolledWindow()
        wv = WebKit.WebView()
        sc.add(wv)
        Gtk.Notebook.append_page(self, tl, sc)
        tl.num = Gtk.Notebook.page_num(sc)
        wv.load_uri(url)
        tl.Label.set_label(wv.get_title())
        tl.show()
        sc.show_all()


