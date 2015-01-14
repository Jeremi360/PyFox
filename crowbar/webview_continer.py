from gi.repository import Gtk, WebKit
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import crowbar

class WebViewContiner(Gtk.ScrolledWindow):
    def __init__(self, notebook, url = None):
        Gtk.ScrolledWindow.__init__(self)
        self.webview = WebKit.WebView()
        self.add(self.webview)
        self.notebook = notebook
        self.ts = crowbar.TabSwitcher(self.notebook, self)

        self.webview.connect("title-changed", self.title_chang)
        self.webview.connect("icon-loaded", self.load_icon)
        self.webview.connect("context-menu", self.open_context_menu)

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

    def title_chang(self, webview, frame, title):

        short = crowbar.make_short(title)
        self.ts.set_label(short)
        self.ts.set_tooltip(title)

        self.notebook.maincotrols.set_title(title)
        self.notebook.maincotrols.auto_set_TabSwitcher_width()

    def load_icon(self, webview, url):
        try:
            pixbuf = webview.get_icon_pixbuf()
            self.notebook.tabcontrols.urlen.set_icon_from_pixbuf(
                                                                 Gtk.EntryIconPosition.PRIMARY,
                                                                 pixbuf
                                                                 )
            upb = self.notebook.tabcontrols.urlen.get_icon_pixbuf(Gtk.EntryIconPosition.PRIMARY)
            self.ts.get_image().set_from_pixbuf(upb)
            self.notebook.maincotrols.Icon.set_from_pixbuf(upb)

        except:
            self.ts.get_image().set_from_icon_name(
                                                   "applications-internet",
                                                   Gtk.IconSize.BUTTON
                                                   )
            self.notebook.tabcontrols.urlen.set_icon_from_icon_name(
                                                                    Gtk.EntryIconPosition.PRIMARY,
                                                                    "applications-internet"
                                                                    )
            self.notebook.maincotrols.Icon.set_from_icon_name(
                                                              "applications-internet",
                                                              Gtk.IconSize.BUTTON
                                                              )
        
    def open_context_menu(self, context_menu, event, hit_test_result, user_data):
        
        context_menu. = WebKit.ContextMenuAction.OPEN_LINK_IN_NEW_WINDOW
        
        
        
        
        
        
        
        
