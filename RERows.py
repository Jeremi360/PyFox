#!/usr/bin/env python

from gi.repository import Gtk, GdkPixbuf, WebKit
import os, sys
import urllib

UI_tab = os.path.join("ui", "Tab.ui")

class Tab:
	def __init__(self):
		self.ui = Gtk.Builder()
		self.ui.add_from_file(UI_tab)
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

UI_main = os.path.join("ui", "Main.ui")

class Browser(Gtk.Window):
	def __init__(self, *args, **kwargs):
		super(Browser, self).__init__(*args, **kwargs)

		# create notebook and tabs
		self.notebook = Gtk.Notebook()
		self.notebook.set_scrollable(True)

		# basic stuff
		self.tabs = []
		self.set_size_request(400, 400)

		# create a first, empty browser tab
		self.tabs.append((self._create_tab(), Gtk.Label("New Tab")))
		self.notebook.append_page(*self.tabs[0])
		self.add(self.notebook)

		# connect signals
		self.connect("destroy", Gtk.main_quit)
		self.connect("key-press-event", self._key_pressed)
		self.notebook.connect("switch-page", self._tab_changed)

		self.notebook.show()
		self.show()

	def _tab_changed(self, notebook, current_page, index):
		if not index:
			return
		title = self.tabs[index][0].webview.get_title()
		if title:
			self.set_title(title)

	def _title_changed(self, webview, frame, title):
		current_page = self.notebook.get_current_page()

		counter = 0
		for tab, label in self.tabs:
			if tab.webview is webview:
				label.set_text(title)
				if counter == current_page:
					self._tab_changed(None, None, counter)
				break
			counter += 1

	def _create_tab(self):
		tab = Tab()
		tab.webview.connect("title-changed", self._title_changed)
		return tab



if __name__ == "__main__":
	app = Browser()
	Gtk.main()

