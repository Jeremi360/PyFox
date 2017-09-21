import os #, sys
#sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pygtkfx
import pyfox

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

TabS_UI = os.path.join(r, "ui", "TabSwitcher.xml")
class TabSwitcher (pygtkfx.Builder):
    def __init__(self, notebook, webviewcontiner):
        pygtkfx.Builder.__init__(self, TabS_UI)
        self.button = self.ui.get_object("button")
        self.removeB = self.ui.get_object("RemoveButton")

        self.webviewcontiner = webviewcontiner
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
        self.button.set_tooltip_text(tooltip)

    def on_tab(self, button):
        page_num = self.notebook.page_num(self.webviewcontiner)
        self.notebook.set_current_page(page_num)
        self.notebook.tabcontrols.set_webview(self.webviewcontiner.webview)

    def on_remove(self, button):
        tf = pyfox.loadPydFile(pyfox.trashFile)
        if tf == None:
            tf = []
        
        wvc = self.webviewcontiner
        nblist = wvc.get_backlist()
        
        nblist.append(wvc.get_current_history_item())
        tf.append(nblist)
        pyfox.savePydFile(pyfox.trashFile, tf)

        page_num = self.notebook.get_current_page()
        self.notebook.remove_page(page_num)
        self.notebook.maincontrols.parent.remove(self.get())

        nwvc = self.notebook.get_current_page_child()
        self.notebook.maincontrols.set_title(nwvc.get_current_title())
        self.notebook.tabcontrols.urlen.set_text(nwvc.get_current_uri())
        
        self.notebook.auto_show_switcher()
        self.notebook.maincontrols.auto_set_TabSwitcher_width()
        self.webviewcontiner = nwvc     
        self.notebook.maincontrols.TarshB.set_sensitive(True)

