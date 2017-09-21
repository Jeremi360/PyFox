from gi.repository import Gtk
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pyfox
import math

class Notebook(Gtk.Notebook):
    def __init__(self, tabcontrols, maincontrols):
        Gtk.Notebook.__init__(self)
        self.tabcontrols = tabcontrols
        self.maincontrols = maincontrols
        self.set_show_tabs(False)
        self.rgroup = []

        self.maincontrols.addb.connect("clicked", self.on_add)

    def on_add(self, button):
        self.add_tab()

    def add_tab(self, url = None, active = True):
        wvc = pyfox.WebViewContiner(self, url, active)
        self.append_page(child = wvc)
        self.maincontrols.TabsSwitcher.add(wvc.ts.get())
        wvc.ts.webviewcontiner = wvc

        group = self.get_nth_page(0).ts.get_group()

        wvc.ts.join_group(group)

        if group not in self.rgroup:
            self.rgroup.append(group)

        self.tabcontrols.set_webview(wvc.webview)
        
        wvc.ts.button.set_active(active)

        if active:
            self.set_current_page(self.page_num(wvc))

        self.maincontrols.auto_set_TabSwitcher_width()
        self.auto_show_switcher()

        return wvc

    def auto_show_switcher(self):
        if self.get_n_pages() > 1:
            self.maincontrols.TBox.hide()
            self.maincontrols.sc.show_all()

        else:
            self.maincontrols.sc.hide()
            self.maincontrols.TBox.show()

    def get_page(self, child):
        return self.get_nth_page(self.page_num(child))

    def get_current_page_child(self):
        return self.get_nth_page(self.get_current_page())