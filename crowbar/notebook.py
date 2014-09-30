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
    def __init__(self, notebook, webview):
        grabbo.Builder.__init__(self, TabS_UI)
        self.button = self.ui.get_object("button")
        self.removeB = self.ui.get_object("RemoveButton")

        self.webview = webview
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

    def get_num(self):
        return self.notebook.page_num(self.webview)

    def on_tab(self, button):
        self.notebook.set_current_page(self.get_num())
        self.notebook.tabcontrols.set_webview(self.webview)

    def on_remove(self, button):
        self.notebook.remove_page(self.get_num())
        self.notebook.maincotrols.remove(self)
        self.notebook.auto_show_switcher()

class WebViewContiner(Gtk.ScrolledWindow):
    def __init__(self, url = None, notebook):
        Gtk.ScrolledWindow.__init__(self)
        self.webview = WebKit.WebView()
        self.add(self.webview)
        self.ts = TabSwitcher(notebook, self.webview)

        self.webview.connect("title-changed", self.title_chang)
        self.webview.connect("icon-loaded", self.load_icon)

        try:
            self.webview.load_uri(url)
        except:
            pass

        self.show_all()

    def title_chang(self, webview, frame, title):

        short = self.make_short(title)
        self.ts.set_label(short)
        self.ts.set_tooltip(title)

        self.notebook.MC.set_title(title)

    def load_icon(self, webview, url):
        try:
            pixbuf = webview.get_icon_pixbuf()
            self.ts.get_image().set_from_pixbuf(pixbuf)

        except:
            self.ts.get_image().set_from_icon_name("applications-internet", Gtk.IconSize.BUTTON)


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

        self.maincotrols.TabsSwitcher.add(wvc.ts.get())

        try:
            wvc.ts.join_group(self.rgroup[0])
        except:
            self.rgroup.append(wvc.ts.get_group())

        if active:
            wvc.ts.button.set_active(True)
            self.tabcontrols.set_webview(wvc.webview)

        self.auto_show_switcher()

    def auto_show_switcher(self):
        if self.get_n_pages() > 1:
            self.maincotrols.Title.hide()
            self.maincotrols.sc.show_all()

        else:
            self.maincotrols.sc.hide()
            self.maincotrols.Title.show()





