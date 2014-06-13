#!/usr/bin/env python

from gi.repository import Gtk, WebKit
import os, pickle

UI_FILE = os.path.join("ui", "Tab.ui")
home = os.path.expanduser("~")
SettingsDir = os.path.join(home, ".rerows")


class Tab(object):
	def __init__(self):

		self.bookfile = os.path.join(SettingsDir, "bookmarks")

		#create settings:
		if not os.path.exists(SettingsDir):
			os.mkdir(SettingsDir)

			#books
			books = []
			f = open(self.bookfile, "wb")
			pickle.dump(books, f)
			f.close()

		#load settings:
		#books
		f = open(self.bookfile, "rb")
		self.books = pickle.load(f)
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

		self.back.connect("clicked", lambda x: self.go_back())
		self.next.connect("clicked", lambda x: self.go_next())
		self.fresh.connect("clicked", lambda x: self.webview.reload())
		self.top.connect("clicked", lambda x: self.scroll_to_top())
		self.find.connect("clicked", lambda x: self.findbox_show())
		self.book.connect("notify::active", lambda x: self.on_book())

		self.closefb = self.ui.get_object("closefb")
		self.closefb.connect("clicked", lambda x: self.findbox_hide())

		self.findfb = self.ui.get_object("findfb")
		self.findfb.connect("activate", lambda x:self.on_find())

		self.backfb = self.ui.get_object("backfb")
		self.backfb.connect("clicked", lambda x: self.find_back())

		self.nextfb = self.ui.get_object("nextfb")
		self.nextfb.connect("clicked", lambda x: self.find_next())

		self.zoomin.connect("clicked", lambda x: self.webview.zoom_in())
		self.zoomout.connect("clicked", lambda x: self.webview.zoom_out())
		self.zoomres.connect("clicked", lambda x: self.webview.set_zoom_level(1.0))
		self.webview.set_full_content_zoom(True)

		self.settings = self.webview.get_property("settings")
		self.settings.set_property("enable-plugins", False)

		self.webview.show()

		self.window = self.ui.get_object("window")
		self.window.set_title("RERows")
		self.window.maximize()
		self.window.show()

	def ch_books(self):
		if self.webview.get_uri() in self.books:
			self.book.set_active(True)
		else:
			self.book.set_active(False)

	def go_back(self):
		self.webview.go_back()
		self.ch_books()

	def go_next(self):
		self.webview.go_forward()
		self.ch_books()


	def on_find(self):
		self.webview.search_text(self.findfb.get_text(), False, True, True)

	def find_back(self):
		self.webview.search_text(self.findfb.get_text(), False, False, True)

	def find_next(self):
		self.webview.search_text(self.findfb.get_text(), False, True, True)

	def scroll_to_top(self):
		self.scroll.do_scroll_child(self.scroll, Gtk.ScrollType.START, False)

	def on_book(self):

		if self.book.get_active():
			if self.url.get_text() in self.books:
				print(self.url.get_text(), "is booked")

			else:
				self.books.append(self.url.get_text())
				f = open(self.bookfile, "wb")
				pickle.dump(self.books, f)
				f.close()
				print(self.url.get_text(), "is now booked")

		else:
			self.books.remove(self.url.get_text())
			f = open(self.bookfile, "wb")
			pickle.dump(self.books, f)
			f.close()


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

	def load_icon(self, webview, url):
		try:
			pixbuf = self.webview.try_get_icon_pixbuf()
			self.url.set_icon_from_pixbuf(Gtk.EntryIconPosition.PRIMARY, pixbuf)
		except:
			self.url.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY, "applications-internet")

	def progress_load(self, webview, amount):
		self.url.set_progress_fraction(amount / 100.0)

	def finish_load(self, webview, frame):
		self.url.set_progress_fraction(0.0)
		self.url.set_text(self.webview.get_uri())

		if self.webview.get_uri() in self.books:
			self.book.set_active(True)
		else:
			self.book.set_active(False)

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
