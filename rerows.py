#!/usr/bin/env python

from gi.repository import Gtk, WebKit
import os, pickle

UI_FILE = os.path.join("ui", "Tab.ui")
home = os.path.expanduser("~")
SettingsDir = os.path.join(home, ".rerows")


class Browser(object):
	def __init__(self):

		self.bookfile = os.path.join(SettingsDir, "bookmarks")

		#create settings:
		if not os.path.exists(SettingsDir):
			os.mkdir(SettingsDir)

			#bookmarks
			bookmarks = []
			f = open(self.bookfile, "wb")
			pickle.dump(bookmarks, f)
			f.close()

		#load settings:
		#bookmarks
		f = open(self.bookfile, "rb")
		self.bookmarks = pickle.load(f)
		f.close()

		self.ui = Gtk.Builder()
		self.ui.add_from_file(UI_FILE)
		self.ui.connect_signals(self)

		self.back = self.ui.get_object("back")
		self.next = self.ui.get_object("next")
		self.url = self.ui.get_object("url")
		self.fresh = self.ui.get_object("fresh")
		self.top = self.ui.get_object("top")
		self.zoomin = self.ui.get_object("zoomin")
		self.zoomres = self.ui.get_object("zoomres")
		self.zoomout = self.ui.get_object("zoomout")
		self.findbox = self.ui.get_object("findbox")
		self.find = self.ui.get_object("find")
		self.book = self.ui.get_object("book")
		self.findbox.hide()

		self.webview = WebKit.WebView()
		self.scroll = self.ui.get_object("scroll")
		self.scroll.add(self.webview)

		self.webview.connect("title-changed", self.title_chang)
		self.webview.connect("icon-loaded", self.load_icon)
		self.webview.connect("load-finished", self.finish_load)
		self.webview.connect("load-progress-changed", self.progress_load)

		self.back.connect("clicked", lambda x: self.webview.go_back())
		self.next.connect("clicked", lambda x: self.webview.go_forward())
		self.fresh.connect("clicked", lambda x: self.webview.reload())
		self.top.connect("clicked", lambda x: self.scroll.do_scroll_child(self.scroll, Gtk.ScrollType.START, False))
		self.find.connect("clicked", lambda x: self.findbox_show())
		#self.book.connect("clicked", lambda x: self.bookit())

		closefb = self.ui.get_object("closefb")
		closefb.connect("clicked", lambda x: self.findbox_hide())

		findfb = self.ui.get_object("findfb")
		findfb.connect("activate", lambda x: self.webview.search_text(findfb.get_text(), False, True, True))

		backfb = self.ui.get_object("backfb")
		backfb.connect("clicked", lambda x: self.webview.search_text(findfb.get_text(), False, False, True))

		nextfb = self.ui.get_object("nextfb")
		nextfb.connect("clicked", lambda x: self.webview.search_text(findfb.get_text(), False, True, True))

		self.zoomin.connect("clicked", lambda x: self.webview.zoom_in())
		self.zoomout.connect("clicked", lambda x: self.webview.zoom_out())
		self.zoomres.connect("clicked", lambda x: self.webview.set_zoom_level(1.0))
		self.webview.set_full_content_zoom(True)

		self.webview.show()

		self.window = self.ui.get_object("window")
		self.window.set_title("RERows")
		self.window.maximize()
		self.window.show()

	def bookit(self):
		if self.webview.get_uri() in self.bookmarks:
			self.book.set_active(True)

			if not self.book.get_active():
				self.bookmarks.remove(self.webview.get_uri())
				f = open(self.bookfile, "wb")
				pickle.dump(self.bookmarks, f)
				f.close()
				print("booked", self.webview.get_uri())

		if self.get_active():
			self.bookmarks.append(self.webview.get_uri())
			f = open(self.bookfile, "wb")
			pickle.dump(self.bookmarks, f)
			f.close()
			print("unbooked", self.webview.get_uri())



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
		self.window.set_title("RERows:" + title)

	def load_icon(self, webview, url):
		try:
			pixbuf = self.webview.get_icon_pixbuf()
			self.url.set_icon_from_pixbuf(Gtk.EntryIconPosition.PRIMARY, pixbuf)
		except:
			self.url.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY, "applications-internet")

	def progress_load(self, webview, amount):
		self.url.set_progress_fraction(amount / 100.0)

	def finish_load(self, webview, frame):
		self.url.set_text(self.webview.get_uri())

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
	app = Browser()
	Gtk.main()


