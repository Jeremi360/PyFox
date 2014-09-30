from gi.repository import Gtk, WebKit
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import crowbar

class WebViewContiner(Gtk.ScrolledWindow):
    def __init__(self, notebook, url = None):
        Gtk.ScrolledWindow.__init__(self)
        self.webview = WebKit.WebView()
        self.add(self.webview)
        self.ts = crowbar.TabSwitcher(notebook, self.webview)

        self.webview.connect("title-changed", self.title_chang)
        self.webview.connect("icon-loaded", self.load_icon)

        try:
            self.webview.load_uri(url)
        except:
            pass

        self.show_all()

    def make_short(self, title, lenght = 26):
        short = ""

        if len(title) > lenght:
            for i in range(lenght):
                try:
                    short += title[i]
                except:
                    pass

        else:
            short = title

        return short

    def title_chang(self, webview, frame, title):

        short = self.make_short(title)
        self.ts.set_label(short)
        self.ts.set_tooltip(title)

        self.notebook.MC.set_title(title)

    def load_icon(self, webview, url):
        try:
            pixbuf = webview.get_icon_pixbuf()
            self.ts.get_image().set_from_pixbuf(pixbuf)

        except:
            self.ts.get_image().set_from_icon_name("applications-internet", Gtk.IconSize.BUTTON)

