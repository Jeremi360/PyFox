from gi.repository import Gtk
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import crowbar
import grabbo

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

UI_Main = os.path.join(r, 'ui', 'MainControls.ui')
class MainControls(grabbo.Builder):
    def __init__(self, parent):
        grabbo.Builder.__init__(self, UI_Main)

        self.notebook = None
        self.parent = parent
        self.menub = self.ui.get_object("MenuButton")
        self.downs = self.ui.get_object("Downs")
        self.EndBox = self.ui.get_object("EndBox")
        self.TitleBox = self.ui.get_object("TitleBox")
        self.Title = self.ui.get_object("Title")
        self.TBox = self.ui.get_object("Tbox")
        self.Icon = self.ui.get_object("Icon")
        self.sc = self.ui.get_object("scrolledwindow")
        self.addb = self.ui.get_object("AddButton")
        self.TabsSwitcher = self.ui.get_object("TabsSwitcher")
        self.TarshB = self.ui.get_object("Trash")
        self.GroupB = self.ui.get_object("Groups")
        self.DownB = self.ui.get_object("Downs")

        self.menub.get_image().set_from_pixbuf(crowbar.getIcon("icon", "png", 24))
        self.menub.connect("clicked", self.on_menu)
        self.TarshB.connect("clicked", self.on_trash)

        self.set_title()
        self.auto_set_TabSwitcher_width()
        self.sc.hide()

    def set_title(self, title = None):
        if title is None:
            t = crowbar.appName
        else:
            t = crowbar.appName + ": " + title

        self.parent.hb.set_title(t)
        self.Title.set_label(t)

    def auto_set_TabSwitcher_width(self):
        maxw = self.parent.get_allocation().width*0.85
        neww = self.TabsSwitcher.get_allocation().width
        minw = crowbar.tabSize

        if neww <= maxw:
            if neww >= minw:
                self.sc.set_min_content_width(neww)
            else:
                self.sc.set_min_content_width(minw)
        else:
            self.sc.set_min_content_width(maxw)

    def on_menu(self, button):
        po = Gtk.Popover.new(self.menub)
        m = crowbar.Menu(po, self.notebook).get()
        po.add(m)
        po.show()

    def on_trash(self, button):
        TList = Gtk.Popover.new(self.TarshB)
        box = Gtk.Box()
        box.set_orientation(Gtk.Orientation.VERTICAL)
        TList.add(box)

        tl = crowbar.loadPydFile(crowbar.trashFile)

        for i in len(range(1, 10)):

            self.TList_add(tl[i], TList, box)

        TList.show_all()

    def TList_add(self, i, TList, box):
        s = crowbar.make_short(i.get_title(), 10)
        b = Gtk.Button(s)
        b.set_tooltip_text(i.get_title())
        img = Gtk.Image()
        b.set_image(img)

        try:
            pixbuf = i.get_icon_pixbuf()
            b.get_image().set_from_pixbuf(pixbuf)
        except:
            b.get_image().set_from_icon_name("applications-internet")

        def on_button(button):
            self.webview.load_uri(i.get_uri())
            TList.hide()

        b.connect("clicked", on_button)
        box.add(b)
