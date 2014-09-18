from gi.repository import Gtk
from gi.repository import Granite

class PopOverWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="ModeButton Demo")
        self.set_border_width(10)
        button = Gtk.Button("Click me")
        self.add(button)
        popover = Granite.WidgetsPopOver()
        button2 = Gtk.ToggleButton("I'm Inside")

        def onSwitched(self):
            print(button2.get_active())
            popover.hide()

        button2.connect("toggled", onSwitched)
        popover.add_action_widget(button2, 1)

        def onClicked(self):
            popover.move_to_widget(button, True)

        button.connect("clicked", onClicked)

win = PopOverWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()