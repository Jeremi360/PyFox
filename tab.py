# forked from https://gist.github.com/kklimonda/890640
# by Jeremi "jeremi360" Biernacki


from gi.repository import Gtk, GdkPixbuf, WebKit
import os
import urllib
from find import Find

Gtk.ScrolledWindow

UI_tab = os.path.join("ui", "Tab.ui")

class Tab:
	def __init__(self):
		self.ui = Gtk.Builder()
		self.ui.add_from_file(UI_tab)
		self.ui.connect_signals(self)

		self.back = self.ui.get_object("back")
		self.forward = self.ui.get_object("next")
		self.url = self.ui.get_object("url")
		self.progressbar = self.ui.get_object("progressbar")
		self.fresh = self.ui.get_object("fresh")
		self.top = self.ui.get_object("top")
		#self.zoomin = self.ui.get_object("zoomin")
		#self.zoomres = self.ui.get_object("zoomres")
		#self.zoomout = self.ui.get_object("zoomout")
		#self.find = self.ui.get_object("find")
		#self.book = self.ui.get_object("book")
		#self.open = self.ui.get_object("open")
		#self.enginebox = self.ui.get_object("enginebox")

		self.webview = WebKit.WebView()
		scroll = self.ui.get_object("scroll")

		self.top.connect("clicked", lambda x: scroll.scroll_child(self, Gtk.ScrollType.START, False))

		self.webview.connect("title-changed", self.title_chang)
		self.webview.connect("icon-loaded", self.load_icon)
		self.webview.connect("load-finished", self.finish_load)
		self.webview.connect("load-progress-changed", self.progress_load)

		scroll.add(self.webview)

		find_box = Find(self)
		box = self.ui.get_object("box")
		box.pack_start(find_box, False, False, 1)

		self.find.connect("clicked", lambda x: find_box.show())

		box.show_all()

	def on_button(self, button):
		if button.get_stock_id() == Gtk.STOCK_GO_FORWARD:
			self.webview.go_forward()
		elif button.get_stock_id() == Gtk.STOCK_GO_BACK:
			self.webview.go_back()

	def  on_fresh(self, button):
			self.webview.reload()

	def url_active(self, widget):
		url = widget.get_text()
		if not "://" or  not "." in url:
			url = "http://www.google.pl/search?q=" + url
		elif not "http://" in url:
			url = "http://" + url
		self.webview.load_uri(url)


	def title_chang(self, webview, frame, title):
		self.window.set_title(title)

	def load_icon(self, webview, url):
		try:
			f = urllib.request.urlopen(url)
			data = f.read()
			pixbuf_loader = GdkPixbuf.PixbufLoader()
			pixbuf_loader.write(data)
			pixbuf_loader.close()
			pixbuf = pixbuf_loader.get_pixbuf()
			self.url.set_icon_from_pixbuf(Gtk.EntryIconPosition.PRIMARY, pixbuf)
		except:
			self.url.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY, "applications-internet")

	def progress_load(self, webview, amount):
		self.progressbar.set_fraction(amount / 100.0)

	def finish_load(self, webview, frame):
		self.url.set_text(frame.get_uri())

		if self.webview.can_go_back():
			self.back.set_sensitive(True)
		else:
			self.back.set_sensitive(False)
		if self.webview.can_go_forward():
			self.forward.set_sensitive(True)
		else:
			self.forward.set_sensitive(False)

	def destroy(self, window):
		Gtk.main_quit()
