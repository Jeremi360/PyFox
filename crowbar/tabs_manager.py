from gi.repository import Gtk
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from crowbar import Tab
import grabbo

class Tabs_Manager(grabbo.Notebook):
    def __init__(self, mc):
        self.MC = mc
        super(Tabs_Manager, self).__init__(Gtk.Stack())
        self.MC.notebook = self
        self.stack.set_transition_duration(200)
        tt = Gtk.StackTransitionType.SLIDE_LEFT_RIGHT
        self.stack.set_transition_type(tt)
        self.minwidth = 264
        self.maxwidth = self.MC.parent.get_screen().get_width()*0.85

    def on_add(self, button):
        self.add_tab()

    def add_tab(self, url = None, active = False):
        con = Tab(self, url)
        self.add_content(con, active)

    def add_content(self, content, active = False):
        grabbo.Notebook.add_tab(self, content.get(), content.tb, active)

        w = self.switcher.get_allocation().width
        self.set_width(w)

        content.get().show()
        self.sc.show()

    def set_width(self, width):

        if width < self.maxwidth:
            self.sc.set_min_content_width(self.minwidth)

        else:
            self.sc.set_min_content_width(width)

    def get_width(self):
        return self.sc.get_min_content_width()


