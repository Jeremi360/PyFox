from gi.repository import Gtk, WebKit
import os, sys
import crowbar
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
#import crowbar
import grabbo

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

TabS_UI = os.path.join(r, "ui", "TabSwitcher.xml")
class TabSwitcher (grabbo.Builder):
    def __init__(self, notebook, num):
        grabbo.Builder.__init__(self, TabS_UI)
        self.Button = self.ui.get_object("Button")
        self.removeB = self.ui.get_object("RemoveButton")

        self.num = num
        self.notebook = notebook

        self.Button.connect("toggled", self.on_tab)
        self.removeB.connect("clicked", self.on_remove)

    def get(self):
        return self.ui.get_object("box")

    def join_group(self, group):
        self.Button.join_group(group)

    def get_group(self):
        return self.Button

    def set_label(self, label):
        self.Button.set_label(label)

    def get_image(self):
        return self.Button.get_image()

    def on_tab(self, button):
        self.notebook.set_current_page(self.num)

    def on_remove(self, button):
        self.notebook.remove_page(self.num)

class WebView(Gtk.ScrolledWindow):
    def __init__(self, url):
        Gtk.ScrolledWindow.__init__(self)
        self.webview = WebKit.WebView()
        self.add(self.webview)
        self.webview.load_uri(url)
        self.show_all()

class Notebook(Gtk.Notebook):
    def __init__(self, maincontrols):
        Gtk.Notebook.__init__(self)
        self.maincotrols = maincontrols
        self.get_show_tabs(False)
        self.rgroup = []

    def add_tab(self, url = None, active = False):
        wv = WebView(url)
        self.append_page(child = wv)
        num = self.page_num(wv)

        ts = TabSwitcher(self, num)
        self.maincotrols.TabsSwitcher.add(ts)

        try:
            ts.join_group(self.rgroup[0])
        except:
            self.rgroup.append(ts.get_group())

        if active:
            self.ts.Button.do_pressed()




