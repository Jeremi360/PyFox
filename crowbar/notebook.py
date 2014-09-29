from gi.repository import Gtk, WebKit
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import crowbar
import grabbo

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

TabS_UI = os.path.join(r, "ui", "TabSwitcher.xml")
class TabSwitcher (grabbo.Builder):
    def __init__(self, notebook, num):
        grabbo.Builder.__init__(self, TabS_UI)
        self.button = self.ui.get_object("button")
        self.removeB = self.ui.get_object("RemoveButton")

        self.num = num
        self.notebook = notebook

        self.button.connect("toggled", self.on_tab)
        self.removeB.connect("clicked", self.on_remove)

    def get(self):
        return self.ui.get_object("box")

    def join_group(self, group):
        self.button.join_group(group)

    def get_group(self):
        return self.button

    def set_label(self, label):
        self.button.set_label(label)

    def get_image(self):
        return self.button.get_image()

    def set_tooltip(self, tooltip):
        self.button.set_tooltip(tooltip)

    def on_tab(self, button):
        self.notebook.set_current_page(self.num)
        wv = self.notebook.get_nth_page(self.num).webwview
        self.notebook.tabcontrols.set_webview(wv)

    def on_remove(self, button):
        self.notebook.remove_page(self.num)
        self.notebook.maincotrols.remove(self)
        self.notebook.auto_show_switcher()

class WebViewContiner(Gtk.ScrolledWindow):
    def __init__(self, url):
        Gtk.ScrolledWindow.__init__(self)
        self.webview = WebKit.WebView()
        self.add(self.webview)
        self.webview.load_uri(url)
        self.show_all()

class Notebook(Gtk.Notebook):
    def __init__(self, tabcontrols, maincontrols):
        Gtk.Notebook.__init__(self)
        self.tabcontrols = tabcontrols
        self.maincotrols = maincontrols
        self.set_show_tabs(False)
        self.rgroup = []

        self.maincotrols.addb.connect("clicked", self.on_add)

    def on_add(self, button):
        self.add_tab()

    def add_tab(self, url = None, active = False):
        wvc = WebViewContiner(url)
        self.append_page(child = wvc)
        num = self.page_num(wvc)

        ts = TabSwitcher(self, num)
        self.maincotrols.TabsSwitcher.add(ts.get())

        try:
            ts.join_group(self.rgroup[0])
        except:
            self.rgroup.append(ts.get_group())

        if active:
            ts.button.set_active(True)
            self.tabcontrols.set_webview(wvc.webview)

        self.auto_show_switcher()

    def auto_show_switcher(self):
        if self.get_n_pages() > 1:
            self.maincotrols.Title.hide()
            self.maincotrols.sc.show_all()

        else:
            self.maincotrols.sc.hide()
            self.maincotrols.Title.show()





