from gi.repository import Gtk
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pyfox
import pygtkfx

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

UI_Main = os.path.join(r, 'ui', 'MainControls.xml')
class MainControls(pygtkfx.Builder):
    def __init__(self, parent):
        pygtkfx.Builder.__init__(self, UI_Main)

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

        self.menub.get_image().set_from_pixbuf(pyfox.getIcon("icon", "svg", 32))

        self.menub.connect("clicked", self.on_menu)
        self.TarshB.connect("clicked", self.on_trash)

        if not os.path.exists(pyfox.trashFile):
            self.TarshB.set_sensitive(False)
        
        else:
            tl = pyfox.loadPydFile(pyfox.trashFile)
            if tl == None:
                self.TarshB.set_sensitive(False)

        self.set_title()
        self.auto_set_TabSwitcher_width()
        self.sc.hide()

    def set_title(self, title = None):
        if title is None:
            t = pyfox.appName
        else:
            t = pyfox.appName + ": " + title

        self.parent.hb.set_title(t)
        self.Title.set_label(t)

    def auto_set_TabSwitcher_width(self):
        maxw = self.parent.get_allocation().width*pyfox.variable.tabSpace/100
        self.sc.set_min_content_width(maxw)

    def on_menu(self, button):
        po = Gtk.Popover.new(self.menub)
        m = pyfox.Menu(po, self.notebook).get()
        po.add(m)
        po.show()

    def on_trash(self, button):
        TList = Gtk.Popover.new(self.TarshB)
        box = Gtk.Box()
        box.set_orientation(Gtk.Orientation.VERTICAL)
        TList.add(box)

        tl = pyfox.loadPydFile(pyfox.trashFile)
        # print(tl)

        i = 0;
        for item in tl:
            if i < pyfox.trashListLimit:
                id = len(tl) - 1 - i
                b = TrashListButton(tl, id, TList, self.notebook)
                box.add(b)

            else:
                break

            i += 1

        TList.show_all()
       

class TrashListButton(Gtk.Button):
    def __init__(self, i, id, TList, notebook):
        self.notebook = notebook
        self.id = id
        i = i[id][-1]
        print(i)
        
        s = ""
        if i["title"] != None:
            s = pyfox.make_short(i["title"], 10, i["uri"])
        
        Gtk.Button.__init__(self, s)
        self.set_tooltip_text(i["uri"])
        img = Gtk.Image()
        self.set_image(img)

        try:
            pixbuf = i.get_icon_pixbuf()
            self.get_image().set_from_pixbuf(pixbuf)
        except:
            self.get_image().set_from_icon_name("applications-internet",
                                                Gtk.IconSize.BUTTON)

        self.connect("clicked", self.on_button)


    def on_button(self, button):
        tf = pyfox.loadPydFile(pyfox.trashFile)
        i = tf[self.id]
        tf.remove(i)
        pyfox.savePydFile(pyfox.trashFile, tf)

        wvc = self.notebook.add_tab(i[-1]["uri"])

        for item in i:
            wvc.add_history_item(item["uri"], item["title"])

        TList.hide()

        
        
