#!/usr/bin/env python

from gi.repository import Gtk, WebKit
import os
import helper

UI_TabButton = os.path.join("ui", "TabButton.ui")

class TabButton(helper.Builder):
	def __init__(self, tab, group):
		super(TabButton, self).__init__(UI_TabButton)

		#get objects from UI_TabButton
		self.icon = self.ui.get_object("Icon")
		self.label = self.ui.get_object("label")
		self.close = self.ui.get_object("Close")

		#connect UI elements with methods
		self.get().connect("toggled", lambda x: self.toggled())
		self.close.connect("clicked", lambda x: self.des())

	def get(self):
		return self.ui.get_object("TabButton")

	def toggled(self):
		pass

	def des(self):
		pass

UI_Tab = os.path.join("ui", "Tab.ui")

class Tab(helper.Builder):
	def __init__(self, group = None):
		super(Tab, self).__init__(UI_Tab)

		self.group = group

		#get objects from UI_Tab
		self.back = self.ui.get_object("back")
		self.next = self.ui.get_object("next")
		self.url = self.ui.get_object("url")
		self.fresh = self.ui.get_object("fresh")
		#self.top = self.ui.get_object("top")
		self.zoomin = self.ui.get_object("zoomin")
		self.zoomres = self.ui.get_object("zoomres")
		self.zoomout = self.ui.get_object("zoomout")
		self.findbox = self.ui.get_object("findbox")
		self.find = self.ui.get_object("find")
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
		self.webview.connect("title-changed", lambda x: self.title_chang())
		self.webview.connect("icon-loaded", lambda x: self.load_icon())
		self.webview.connect("load-finished", lambda x: self.finish_load())
		self.webview.connect("load-progress-changed", lambda x: self.progress_load())

		#connect UI elements with methods
		self.back.connect("clicked", lambda x: self.webview.go_back())
		self.next.connect("clicked", lambda x: self.webview.go_forward())
		self.fresh.connect("clicked", lambda x: self.webview.reload())
		#self.top.connect("clicked", lambda x: self.scroll_to_top())
		self.find.connect("clicked", lambda x: self.findbox_show())
		self.closefb.connect("clicked", lambda x: self.findbox_hide())
		self.findfb.connect("activate", lambda x: self.on_find())
		self.backfb.connect("clicked", lambda x: self.find_back())
		self.nextfb.connect("clicked", lambda x: self.find_next())
		self.zoomin.connect("clicked", lambda x: self.webview.zoom_in())
		self.zoomout.connect("clicked", lambda x: self.webview.zoom_out())
		self.zoomres.connect("clicked", lambda x: self.webview.set_zoom_level(1.0))

		#last settings
		self.webview.set_full_content_zoom(True)

		self.tabbutton = TabButton(self, self.group)

		#show
		self.webview.show()

	def get(self):
		return self.ui.get_object("box")

	def on_find(self):
		self.webview.search_text(self.findfb.get_text(), False, True, True)

	def find_back(self):
		self.webview.search_text(self.findfb.get_text(), False, False, True)

	def find_next(self):
		self.webview.search_text(self.findfb.get_text(), False, True, True)

	def scroll_to_top(self):
		self.scroll.do_scroll_child(self.scroll, Gtk.ScrollType.START, False)

	def on_book(self):
		print("to dev")

	def findbox_show(self):
		self.find.hide()
		self.findbox.show()

	def findbox_hide(self):
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
		self.window.set_title("RERows - " + title)
		if self.tabbutton != None:
			self.tabbutton.label.set_label(title)

	def load_icon(self, webview, url):
		try:
			pixbuf = webview.try_get_favicon_pixbuf()
			self.url.set_icon_from_pixbuf(Gtk.EntryIconPosition.PRIMARY, pixbuf)

			if self.tabbutton != None:
				self.tabbutton.icon.set_from_pixbuf(Gtk.EntryIconPosition.PRIMARY, pixbuf)

		except:
			self.url.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY, "applications-internet")

			if self.tabbutton != None:
				self.tabbutton.icon.set_from_icon_name(Gtk.EntryIconPosition.PRIMARY, "applications-internet")

	def progress_load(self, webview, amount):
		self.url.set_progress_fraction(amount / 100.0)

	def finish_load(self, webview, frame):
		self.url.set_text(frame.get_uri())
		self.url.set_progress_fraction(0.0)

		if self.webview.can_go_back():
			self.back.set_sensitive(True)
		else:
			self.back.set_sensitive(False)
		if self.webview.can_go_forward():
			self.next.set_sensitive(True)
		else:
			self.next.set_sensitive(False)

class Window(helper.Window):
	def __init__(self):
		T = Tab(self).get()
		super(Window, self).__init__(T)

if __name__ == "__main__":
	app = Window()
	Gtk.main()
