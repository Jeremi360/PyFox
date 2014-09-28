from gi.repository import Gtk, WebKit
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import crowbar
import grabbo

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

TabL_UI = os.path.join(r, "ui", "TabLabel.xml")
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
    def __init__(self, tabcontrols):
        Gtk.Notebook.__init__(self)
        self.set_scrollable(True)
        self.tabc = tabcontrols

    def append_page(self, url = None):
        tl = TabLabel(self)
        sc = Gtk.ScrolledWindow()
        wv = WebKit.WebView()
        sc.add(wv)
        Gtk.Notebook.append_page(self, tl, sc)
        tl.num = Gtk.Notebook.page_num(sc)
        self.set_webview(wv, url)
        tl.Label.set_label(wv.get_title())
        tl.show()
        sc.show_all()

    def set_webview(self, wv, url):
        #connect WEBVIEW signals with methods
        wv.connect("title-changed", self.tabc.title_chang)
        wv.connect("icon-loaded", self.tabc.load_icon)
        wv.connect("load-finished", self.tabc.finish_load)
        wv.connect("load-progress-changed", self.tabc.progress_load)

        wv.set_full_content_zoom(True)

        self.tabc.urlen.set_text(url)






