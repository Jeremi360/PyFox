from gi.repository import Gtk, WebKit
import os, sys
from _ast import Num
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import crowbar
import grabbo

TabL_UI = os.path.join(crowbar.appdir, "ui", "TabLabel.xml")
class TabLabel (grabbo.Builder):
    def __init__(self, notebook, num, label, tooltip):
        grabbo.Builder.__init__(self, TabL_UI)
        self.Label = self.ui.get_object("label")
        self.Icon = self.ui.get_object("icon")
        self.Button = self.ui.get_object("button")

        self.num = num
        self.notebook = notebook
        self.Label.set_label(label)
        self.Label.set_tooltip_text(tooltip)

        self.Button.connect("clicked", self.on_button)

    def get(self):
        return self.ui.get_object("box")

    def on_button(self, button):
        self.notebook.remove_page(self.num)


class Notebook(Gtk.Notebook):
    def __init__(self):
        Gtk.Notebook.__init__(self)

    def append_page(self, url):


