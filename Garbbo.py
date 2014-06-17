# small lib to make Gtk in my way
# warning this is special frok of Grabbo for RERows
# Grabbo def: http://en.wikipedia.org/wiki/Gabbro

from gi.repository import Gtk

try:
    from gi.repository.Granite import WidgetsPopOver as Pop
except:
    pass

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
        self.box = Gtk.VBox()
        self.vp.add(self.box)
        self.scroll.add(self.vp)

        if addable:
            box = Gtk.VBox()
            ar = Builder(UI_AR)
            add = ar.ui.get_object("add")
            remove = ar.ui.get_object("remove")

            ar.show()
            box.pack_start(ar, False, False, 0)
            box.pack_end(self.scroll, True, True, 0)

        else:
            self.add(self.scroll)

        self.show_all()

    def on_element(self, element):
        print(element[1])

    def do_set_icon(self, e, element):
        pass

    def on_remove(self, box, element):
        del self.list[element[0]]
        del box

    def add_element(self, element = ["title", "url"]):
        self.list[element[0]:element[1]]
        box = Builder(UI_ListE)
        e = box.ui.get_object("element")
        e.do_set_label('title')
        e.connect("clicked", lambda x: self.on_element(element))
        self.set_icon(e, element)
        r = box.ui.get_object("remove")
        r.connect("clicked", lambda x: self.on_remove(box, element))
        self.box.pack_start(box, False, False, 0)
        self.box.show()


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
