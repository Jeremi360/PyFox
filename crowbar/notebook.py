from gi.repository import Gtk
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import crowbar

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
        wvc = crowbar.WebViewContiner(self, url)
        self.append_page(child = wvc)

        self.maincotrols.TabsSwitcher.add(wvc.ts.get())

        try:
            wvc.ts.join_group(self.rgroup[0])
        except:
            self.rgroup.append(wvc.ts.get_group())

        if active:
            wvc.ts.button.set_active(True)
            self.tabcontrols.set_webview(wvc.webview)

        new_tab_size = wvc.ts.get_group().get_prefered_width()[0] #hear
        self.maincotrols.auto_set_TabSwitcher_width()
        self.auto_show_switcher()

    def auto_show_switcher(self):
        if self.get_n_pages() > 1:
            self.maincotrols.TBox.hide()
            self.maincotrols.sc.show_all()

        else:
            self.maincotrols.sc.hide()
            self.maincotrols.TBox.show()
