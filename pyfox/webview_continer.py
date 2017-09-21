import gi
gi.require_version('WebKit', '3.0')
from gi.repository import Gtk, WebKit
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pyfox

class WebViewContiner(Gtk.ScrolledWindow):
    def __init__(self, notebook, url = None, show = True):
        Gtk.ScrolledWindow.__init__(self)
        self.webview = WebKit.WebView()
        self.add(self.webview)
        self.notebook = notebook
        self.ts = pyfox.TabSwitcher(self.notebook, self)

        self.webview.connect("title-changed", self.title_changed)
        self.webview.connect("icon-loaded", self.load_icon)
        self.webview.connect("context-menu", self.open_context_menu)

        if show:
            self.notebook.tabcontrols.urlen.set_text("")
            nt = "New Tab"
            self.notebook.tabcontrols.urlen.set_icon_from_icon_name(
                                                                    Gtk.EntryIconPosition.PRIMARY,
                                                                    "applications-internet"
                                                                    )

        self.ts.get_image().set_from_icon_name(
                                                "applications-internet",
                                                Gtk.IconSize.BUTTON
                                                )
        self.ts.set_label(nt)
        self.ts.set_tooltip(nt)

        try:
            self.webview.load_uri(url)
        except:
            pass

        self.show_all()

    def title_changed(self, webview, frame, title):

        short = pyfox.make_short(title)
        self.ts.set_label(short)
        self.ts.set_tooltip(title)

        self.notebook.maincontrols.set_title(title)
        self.notebook.maincontrols.auto_set_TabSwitcher_width()

    def load_icon(self, webview, url):
        try:
            pixbuf = webview.get_icon_pixbuf()
            self.notebook.tabcontrols.urlen.set_icon_from_pixbuf(
                                                                 Gtk.EntryIconPosition.PRIMARY,
                                                                 pixbuf
                                                                 )

            upb = self.notebook.tabcontrols.urlen.get_icon_pixbuf(Gtk.EntryIconPosition.PRIMARY)
            self.ts.get_image().set_from_pixbuf(upb)
            self.notebook.maincontrols.Icon.set_from_pixbuf(upb)

        except:
            self.ts.get_image().set_from_icon_name(
                                                   "applications-internet",
                                                   Gtk.IconSize.BUTTON
                                                   )

            self.notebook.tabcontrols.urlen.set_icon_from_icon_name(
                                                                    Gtk.EntryIconPosition.PRIMARY,
                                                                    "applications-internet"
                                                                    )

            self.notebook.maincontrols.Icon.set_from_icon_name(
                                                              "applications-internet",
                                                              Gtk.IconSize.BUTTON
                                                              )

    def open_context_menu(self,
                          context_menu,
                          event,
                          hit_test_result,
                          user_data):

        pass
    
    def get_backlist(self):
        nblist = []
        bflist = self.webview.get_back_forward_list()
        l = bflist.get_back_length()
        blist = bflist.get_back_list_with_limit(l)
        for item in blist:
            nblist.append({"title":item.get_title(), "uri":item.get_uri()})

        return nblist
    
    def get_current_title(self):
        return self.webview.get_title()
    
    def get_current_uri(self):
        return self.webview.get_uri()
    
    def get_current_history_item(self):
        return {
                "title":self.get_current_title(),
                "uri":self.get_current_uri()
                }
    
    def add_history_item(self, title, uri):
        hi = WebKit.WebHistoryItem.new_with_data(uri, title)
        self.webview.get_back_forward_list().add_item(hi)