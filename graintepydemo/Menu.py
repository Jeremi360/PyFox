#!/usr/bin/env python

from gi.repository import Granite
from gi.repository import Gtk

window = Gtk.Window.new(Gtk.WindowType.TOPLEVEL)
toolbar = Gtk.Toolbar.new()
toolbar.get_style_context().add_class("primary-toolbar")
window.add(toolbar)

menu = Gtk.Menu.new()
menu.append(Gtk.MenuItem.new_with_label("Hello World"))

appmenu = Granite.WidgetsAppMenu.new(menu)
toolbar.insert(appmenu, -1)
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()