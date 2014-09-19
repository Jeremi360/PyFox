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

home = os.path.expanduser("~")
conf = os.path.join(home,'.crowbar')


class Tabs_Manager(grabbo.Notebook):
    def __init__(self, mc):
        self.MC = mc
        super(Tabs_Manager, self).__init__(Gtk.Stack())
        self.MC.notebook = self

    def on_add(self, button):
        self.add_tab()

    def add_tab(self, url = None, active = False):
        con = Tab(self, url)
        self.add_content(con, active)

    def add_content(self, content, active = False):
        grabbo.Notebook.add_tab(self, content.get(), content.tb)

        w = self.get_width() + 210
        self.set_width(w)

        if active:
            content.tb.button.set_mode(True)
            self.stack.set_visible_child(content.get())

        content.get().show()
        self.sc.show()

    def set_width(self, width):
        w = self.MC.parent.get_screen().get_width()
        if width < w*0.85:
            self.sc.set_min_content_width(width)

    def get_width(self):
        return self.sc.get_min_content_width()

UI_Main = os.path.join(r, 'ui', 'Main.xml')
class Main_Controls(grabbo.Builder):
    def __init__(self, parent):
        grabbo.Builder.__init__(self, UI_Main)

        self.notebook = None
        self.parent = parent
        self.menub = self.ui.get_object("MenuButton")
        self.downs = self.ui.get_object("Downs")
        self.StartBox = self.ui.get_object("StartBox")
        self.EndBox = self.ui.get_object("EndBox")

        self.menub.connect("clicked", self.on_menu)

    def set_title(self, title):
        self.parent.hb.set_title(variable.appname + ": " + title)

    def on_menu(self, button):
        po = Gtk.Popover.new(self.menub)
        po.set_pointing_to(self.menub.get_allocation())
        m = menu.Menu(po, self.notebook).get()
        po.add(m)
        po.show()

class Window(grabbo.Window):
    def __init__(self):
        super(Window, self).__init__()
        self.MC = Main_Controls(self)

        self.set_icon_from_file(variable.icon)

        self.tabs = Tabs_Manager(self.MC)

        self.tabs.add_tab(variable.home)

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
    app = Window()
    Gtk.main()
