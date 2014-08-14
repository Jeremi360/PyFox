from gi.repository import Gtk, WebKit
import grabbo
import os

UI_Tab = os.path.join('..', 'ui', 'Tab.ui')

class Tab(grabbo.Builder):
	def __init__(self, TB, url = None, paronama = None):
		super(Tab, self).__init__(UI_Tab)

		self.paronama = paronama
		self.TB = TB

		#get objects from UI_Tab
		#main tab toolbar
		self.back = self.ui.get_object("back")
		self.next = self.ui.get_object("next")
		self.urlen = self.ui.get_object("urlen")
		self.fresh = self.ui.get_object("fresh")
		self.zoomin = self.ui.get_object("zoomin")
		self.zoomres = self.ui.get_object("zoomres")
		self.zoomout = self.ui.get_object("zoomout")
		self.find = self.ui.get_object("find")
		self.book = self.ui.get_object("book")
		self.ExtBox = self.ui.get_object("ExtBox")

		#findbox
		self.findbox = self.ui.get_object("findbox")
		self.closefb = self.ui.get_object("closefb")
		self.findfb = self.ui.get_object("findfb")
		self.backfb = self.ui.get_object("backfb")
		self.nextfb = self.ui.get_object("nextfb")

		#this UI elements are hide until is not in use
		self.findbox.hide()

		#create WEBVIEW
		self.webview = WebKit.WebView()
		self.scroll = self.ui.get_object("scroll")
		self.scroll.add(self.webview)

		#connect WEBVIEW signals with methods
		self.webview.connect("title-changed", self.title_chang)
		self.webview.connect("icon-loaded", self.load_icon)
		self.webview.connect("load-finished", self.finish_load)
		self.webview.connect("load-progress-changed", self.progress_load)

		#connect UI elements with methods

		#main tab toolbar
		self.back.connect("clicked", self.webview.go_back)
		self.next.connect("clicked", self.webview.go_forward)
		self.fresh.connect("clicked", self.webview.reload)
		self.find.connect("toggled", self.on_findbox)
		self.zoomin.connect("clicked", self.webview.zoom_in)
		self.zoomout.connect("clicked", self.webview.zoom_out)
		self.zoomres.connect("clicked",  self.reset_zoom)

		#findbox
		self.findfb.connect("activate", self.on_find())
		self.backfb.connect("clicked", self.find_back())
		self.nextfb.connect("clicked", self.find_next())

		#last settings
		self.webview.set_full_content_zoom(True)

		if url:
			self.urlen.set_text(url)
			self.webview.load_uri(url)

		#show
		self.webview.show()

	def get(self):
		return self.ui.get_object("box")

	def reset_zoom(self, button):
		self.webview.set_zoom_level(1.0)

	def on_find(self, button):
		self.webview.search_text(
								self.findfb.get_text(),
								False, True, True
								)

	def find_back(self, button):
		self.webview.search_text(
								self.findfb.get_text(),
								False, False, True
								)

	def find_next(self, button):
		self.webview.search_text(
								self.findfb.get_text(),
								False, True, True
								)

	def on_book(self, button):
		pass

	def on_findbox(self, button):
		if self.find.get_active():
			self.findbox.show()
		else:
			self.findbox.hide()

	def url_active(self, widget):
		url = widget.get_text()
		if not "://" or  not "." in url:
			url = "http://www.google.pl/search?q=" + url
		elif not "://" in url:
			url = "http://" + url
		self.webview.load_uri(url)

	def title_chang(self, webview, frame, title):
		short = ""
		for i in range(26):
			try:
				short += title[i]
			except:
				pass

		self.TB.button.set_label(short)
		self.TB.button.set_tooltip_text(title)

	def load_icon(self, webview, url):
		try:
			pixbuf = webview.get_icon_pixbuf()
			self.urlen.set_icon_from_pixbuf(Gtk.EntryIconPosition.PRIMARY, pixbuf)
			img = Gtk.Image()
			img.set_from_pixbuf(self.urlen.get_icon_pixbuf(Gtk.EntryIconPosition.PRIMARY))
			self.TB.button.set_image(img)

		except:
			self.urlen.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY, "applications-internet")
			img = Gtk.Image()
			img.set_from_icon_name("applications-internet", 4)
			self.TB.button.set_image(img)

	def progress_load(self, webview, amount):
		self.urlen.set_progress_fraction(amount / 100.0)

	def finish_load(self, webview, frame):
		self.urlen.set_text(webview.get_uri())
		self.urlen.set_progress_fraction(0.0)

		if self.webview.can_go_back():
			self.back.set_sensitive(True)
		else:
			self.back.set_sensitive(False)
		if self.webview.can_go_forward():
			self.next.set_sensitive(True)
		else:
			self.next.set_sensitive(False)
