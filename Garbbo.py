# small lib to make Gtk in my way
# Grabbo def: http://en.wikipedia.org/wiki/Gabbro

from gi.repository import Gtk
from gi.repository.Granite import WidgetsPopOver as PopOver
import os

Logo = os.path.join("icons", "logo.svg")

class Builder(object):
    def __init__(self, UI_FILE):
        #load UI from UI_FILE
        self.ui = Gtk.Builder()
        self.ui.add_from_file(UI_FILE)
        self.ui.connect_signals(self)
        
        
UI_ListE = os.path.join("ui", "ListElement.ui")
UI_AR = os.path.join("ui", "AddRemove.ui")

class List(PopOver):
    def __init__(self, pydict = {"title":"url"}, addable = False):
        self.list = pydict
        
        self.scroll = Gtk.ScrolledWindow()
        self.vp = Gtk.Viewport()
        self.scroll.add(self.vp)
        #self.scroll.set_
        
        if addable:
            box = Gtk.HBox()
            ar = Builder(UI_AR)
            add = ar.ui.get_object("add")
            remove = ar.ui.get_object("remove")
            
            ar.show()
            box.pack_start(ar, False, False, 0)
            box.pack_end(self.scroll, True, True, 0)
            
            
        
    def add_element(self, element):
        self.add()
         
        
        

class Window(Builder, Gtk.Window):
    def __init__(self, content = Gtk.Box()):
        Gtk.Window.__init__(self)
        self.content = content
        self.do_then_init()

        self.set_size_request(400, 400)
        self.add(self.content)
        self.maximize()
        self.set_icon_from_file(Logo)
        self.show()

    def do_then_init(self):
        pass
