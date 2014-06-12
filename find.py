
class Find(Gtk.HBox):
    def __init__(self):

        go_button = Gtk.Button("go to...")
        go_button.connect("clicked", self._load_url)
        self.url_bar = Gtk.Entry()
        self.url_bar.connect("activate", self._load_url)
        self.webview = WebKit.WebView()
        self.show()

        self.go_back = Gtk.Button("Back")
        self.go_back.connect("clicked", lambda x: self.webview.go_back())
        self.go_forward = Gtk.Button("Forward")
        self.go_forward.connect("clicked", lambda x: self.webview.go_forward())

        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.add(self.webview)

        find_box = Gtk.HBox()
        close_button = Gtk.Button("Close")
        close_button.connect("clicked", lambda x: find_box.hide())
        self.find_entry = Gtk.Entry()
        self.find_entry.connect("activate",
                                lambda x: self.webview.search_text(self.find_entry.get_text(),
                                                                   False, True, True))
        prev_button = Gtk.Button("Previous")
        next_button = Gtk.Button("Next")
        prev_button.connect("clicked",
                            lambda x: self.webview.search_text(self.find_entry.get_text(),
                                                               False, False, True))
        next_button.connect("clicked",
                            lambda x: self.webview.search_text(self.find_entry.get_text(),
                                                               False, True, True))
        find_box.pack_start(close_button, False, False, 0)
        find_box.pack_start(self.find_entry, False, False, 0)
        find_box.pack_start(prev_button, False, False, 0)
        find_box.pack_start(next_button, False, False, 0)
        self.find_box = find_box

        url_box = Gtk.HBox()
        url_box.pack_start(self.go_back, False, False, 0)
        url_box.pack_start(self.go_forward, False, False, 0)
        url_box.pack_start(self.url_bar, True, True, 0)
        url_box.pack_start(go_button, False, False, 0)

        self.pack_start(url_box, False, False, 0)
        self.pack_start(scrolled_window, True, True, 0)
        self.pack_start(find_box, False, False, 0)

        url_box.show_all()
        scrolled_window.show_all()

    def _load_url(self, widget):
        url = self.url_bar.get_text()
        if not "://" or  not "." in url:
            url = "http://www.google.pl/search?q=" + url
        elif not "http://" in url:
            url = "http://" + url
        self.webview.load_uri(url)