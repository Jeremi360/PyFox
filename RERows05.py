#!/usr/bin/env python

from gi.repository import Gtk, GdkPixbuf, WebKit
import os, sys
import urllib

UI_FILE = os.path.join("ui", "py beta05 fresh.ui")

class Browser:
	def __init__(self):
		self.ui = Gtk.Builder()
		self.ui.add_from_file(UI_FILE)
		self.ui.connect_signals(self)

		self.back = self.ui.get_object("back")
		self.forward = self.ui.get_object("forward")
		self.url = self.ui.get_object("url")
		self.progressbar = self.ui.get_object("progressbar")
		self.fresh = self.ui.get_object("fresh")

		self.webview = WebKit.WebView()
		scrolled_window = self.ui.get_object("scroll")
		scrolled_window.add(self.webview)

		self.webview.connect("title-changed", self.title_chang)
		self.webview.connect("icon-loaded", self.load_icon)
		self.webview.connect("load-finished", self.finish_load)
		self.webview.connect("load-progress-changed", self.progress_load)

		self.window = self.ui.get_object("window")
		self.window.show_all()

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
			f = urllib.urlopen(url)
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

if __name__ == "__main__":
	app = Browser()
	Gtk.main()

