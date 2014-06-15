#!/usr/bin/env python

from gi.repository import Gtk, WebKit
import os

UI_TabButton = os.path.join("ui", "TabButton.ui")

class TabButton(object):
	def __init__(self, tab, tabgrup):

		#load UI from UI_TabButton
		self.ui = Gtk.Builder()
		self.ui.add_from_file(UI_TabButton)
		self.ui.connect_signals(self)

		#get objects from UI_TabButton
		self.icon = self.ui.get_object("Icon")
		self.label = self.ui.get_object("label")
		self.close = self.ui.get_object("Close")

		#connect UI elements with methods
		self.get().connent("toggled", lambda x: self.toggled())
		self.close.connect("clicked", lambda x: self.des())

	def get(self):
		return self.ui.get_object("TabButton")

	def toggled(self):
		pass

	def des(self):
		pass

UI_Tab = os.path.join("ui", "Tab.ui")

class Tab(object):
	def __init__(self):
		#load UI from UI_Tab
		self.ui = Gtk.Builder()
		self.ui.add_from_file(UI_Tab)
		self.ui.connect_signals(self)

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
		self.bookit = self.ui.get_object("bookit")
		self.unbookit = self.ui.get_object("unbookit")
		self.engine = self.ui.get_object("engine")
		self.closefb = self.ui.get_object("closefb")
		self.findfb = self.ui.get_object("findfb")
		self.backfb = self.ui.get_object("backfb")
		self.nextfb = self.ui.get_object("nextfb")
		self.adds = self.ui.get_object("addbox")

		#hide this - don't work yet:
		self.adds.hide()
		self.engine.hide()
		self.bookit.hide()
		self.unbookit.hide()

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
		self.window = self.ui.get_object("window")
		self.window.set_title("RERows")
		self.window.maximize()

		#show
		self.webview.show()
		self.window.show()

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

	def title_chang(self, tabbutton = None, window = None,  webview, frame, title):
		if window == None:
			self.window.set_title("RERows - " + title)
		else:
			window.set_title("RERows - " + title)
		if tabbutton != None:
			tabbutton.label.set_label(title)

	def load_icon(self, tabbutton = None, webview, url):
		try:
			pixbuf = self.webview.get_icon_pixbuf()
			self.url.set_icon_from_pixbuf(Gtk.EntryIconPosition.PRIMARY, pixbuf)
			if tabbutton != None:
				tabbutton.Icon.set_from_pixbuf(Gtk.EntryIconPosition.PRIMARY, pixbuf)
		except:
			self.url.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY, "applications-internet")
			if tabbutton != None:
				tabbutton.Icon.set_from_pixbuf(Gtk.EntryIconPosition.PRIMARY, "applications-internet")

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

	def destroy(self, window):
		Gtk.main_quit()

if __name__ == "__main__":
	app = Tab()
	Gtk.main()

