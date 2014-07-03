#!/usr/bin/env python

from gi.repository import Gtk, WebKit
import grabbo
import os

UI_TabButton =  os.path.join("ui", "TabButton.ui")

class TabButton(grabbo.Builder):
	def __init__(self, tab, group):
		super(TabButton, self).__init__(UI_TabButton)

		self.group = group
		self.tab = tab

		#get objects from UI_TabButton
		self.button = self.ui.get_object("TabButton")
		self.close = self.ui.get_object("Close")

		#connect UI elements with methods
		self.button.connect("toggled", lambda x: self.toggled)
		self.close.connect("clicked", self.des)

	def get(self):
		return self.ui.get_object("box")

	def toggled(self):
		n = self.group.tabs.get_current_page()
		t = self.group.tabs.page_num(self.tab.get())

		if n != t:
			self.button.set_active(False)
		else:
			self.group.tabs.set_current_page(t)

		if self.button.set_active(True):
			self.group.tabs.set_current_page(t)

	def des(self, button, name):
		pass

UI_Tab = os.path.join("ui", "Tab.ui")

class Tab(grabbo.Builder):
	def __init__(self, group = None):
		super(Tab, self).__init__(UI_Tab)

		self.group = group

		#get objects from UI_Tab
		#main tab toolbar
		self.back = self.ui.get_object("back")
		self.next = self.ui.get_object("next")
		self.url = self.ui.get_object("url")
		self.fresh = self.ui.get_object("fresh")
		#self.top = self.ui.get_object("top")
		self.zoomin = self.ui.get_object("zoomin")
		self.zoomres = self.ui.get_object("zoomres")
		self.zoomout = self.ui.get_object("zoomout")
		self.find = self.ui.get_object("find")
		self.book = self.ui.get_object("book")

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
		self.back.connect("clicked", lambda x: self.webview.go_back())
		self.next.connect("clicked", lambda x: self.webview.go_forward())
		self.fresh.connect("clicked", lambda x: self.webview.reload())
		#self.top.connect("clicked", lambda x: self.scroll_to_top())
		self.find.connect("clicked", lambda x: self.findbox_show())
		self.zoomin.connect("clicked", lambda x: self.webview.zoom_in())
		self.zoomout.connect("clicked", lambda x: self.webview.zoom_out())
		self.zoomres.connect("clicked", lambda x: self.webview.set_zoom_level(1.0))

		#findbox
		self.closefb.connect("clicked", self.findbox_hide)
		self.findfb.connect("activate", self.on_find)
		self.backfb.connect("clicked", self.find_back)
		self.nextfb.connect("clicked", self.find_next)

		#last settings
		self.webview.set_full_content_zoom(True)
		self.TB = TabButton(self, self.group)

		#show
		self.webview.show()

	def get(self):
		return self.ui.get_object("box")

	def on_find(self, button, name):
		self.webview.search_text(self.findfb.get_text(), False, True, True)

	def find_back(self, button, name):
		self.webview.search_text(self.findfb.get_text(), False, False, True)

	def find_next(self, button, name):
		self.webview.search_text(self.findfb.get_text(), False, True, True)

	def scroll_to_top(self, button, name):
		self.scroll.do_scroll_child(self.scroll, Gtk.ScrollType.START, False)

	def on_book(self, button, name):
		pass

	def findbox_show(self, button, name):
		self.find.hide()
		self.findbox.show()

	def findbox_hide(self, button, name):
		self.findbox.hide()
		self.find.show()

	def url_active(self, widget):
		url = widget.get_text()
		if not "://" or  not "." in url:
			url = "http://www.google.pl/search?q=" + url
		elif not "://" in url:
			url = "http://" + url
		self.webview.load_uri(url)

	def title_chang(self, webview, frame, title):
		self.group.set_title("cRoWBaR - " + title)
		if self.TB.button != None:
			self.TB.button.set_label(title)

	def load_icon(self, webview, url):
		try:
			pixbuf = webview.get_favicon_pixbuf()
			self.url.set_icon_from_pixbuf(Gtk.EntryIconPosition.PRIMARY, pixbuf)
			self.TB.button.get_image().set_from_pixbuf(pixbuf)

		except:
			self.url.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY, "applications-internet")
			self.TB.button.get_image().set_from_icon_name("applications-internet", 4)

	def progress_load(self, webview, amount):
		self.url.set_progress_fraction(amount / 100.0)

	def finish_load(self, webview, frame):
		self.url.set_text(webview.get_uri())
		self.url.set_progress_fraction(0.0)

		if self.webview.can_go_back():
			self.back.set_sensitive(True)
		else:
			self.back.set_sensitive(False)
		if self.webview.can_go_forward():
			self.next.set_sensitive(True)
		else:
			self.next.set_sensitive(False)

class Window(grabbo.Window):
	def __init__(self):
		super(Window, self).__init__()

	def do_then_init(self):
		self.content = Tab(self).get()

if __name__ == "__main__":
	app = Window()
	Gtk.main()
