#!/usr/bin/env python3

from gi.repository import Gtk
import os

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

try:
    from crowbar.tab import Tab
    from crowbar import variable
    from crowbar import menu
    print("Eclipse way")
except:
    from tab import Tab
    import variable
    import menu
    print("Normal way")

try:
    import grabbo
except:
    print("Please first install Grabbo in your python path or copy to crowbar dir")
    print("Grabbo can be download from https://github.com/jeremi360/Grabbo")
    exit()


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



class Main(grabbo.Window):
    def __init__(self):
        grabbo.Window.__init__(self)
        self.MC = Main_Controls(self)
        self.set_icon_from_file(variable.icon)

        self.tabs = Tabs_Manager(self.MC)
        self.tabs.add_tab(url = variable.home, active = True)

        self.hb = Gtk.HeaderBar()
        self.hb.set_show_close_button(True)
        self.hb.set_title(variable.appname)
        self.hb.set_custom_title(self.tabs.get())
        self.hb.props.border_width = 0
        self.hb.props.margin = 0
        self.hb.pack_start(self.MC.StartBox)
        self.hb.pack_end(self.MC.EndBox)
        self.hb.set_has_subtitle(False)
        self.set_titlebar(self.hb)

        self.add(self.tabs.stack)

        self.hb.show()
        self.tabs.stack.show()
        self.show()

    def on_close(self, button):
        grabbo.Window.on_close(self, button)

if __name__ == "__main__":
    app = Main()
    Gtk.main()
