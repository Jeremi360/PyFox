#!/usr/bin/env python3

from gi.repository import Gtk
import os

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

try:
    from crowbar import Tab
    from crowbar import variable
    from crowbar import Main_Controls
    from crowbar import Tabs_Manager
    print("Eclipse way")
except:
    from tab import Tab
    import variable
    import Main_Controls
    import Tabs_Manager
    print("Normal way")

try:
    import grabbo
except:
    print("Please first install Grabbo in your python path or copy to crowbar dir")
    print("Grabbo can be download from https://github.com/jeremi360/Grabbo")
    exit()



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
