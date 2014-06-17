#!/usr/bin/env python

from gi.repository import Gtk, WebKit
import os
import Garbbo

UI_TabButton = os.path.join("ui", "TabButton.ui")

class TabButton(Garbbo.Builder):
	def __init__(self, tab, group):
		super(TabButton, self).__init__(UI_TabButton)

		self.group = group
		self.tab = tab

		#get objects from UI_TabButton
		self.button = self.ui.get_object("TabButton")
		self.close = self.ui.get_object("Close")

		#connect UI elements with methods
		self.button.connect("toggled", lambda x: self.toggled())
		self.close.connect("clicked", lambda x: self.des())

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

	def des(self):
		pass


UI_Tab = os.path.join("ui", "Tab.ui")

class Tab(Garbbo.Builder):
	def __init__(self, group = None):
		super(Tab, self).__init__(UI_Tab)
		self.group = group
		self.do_then_init()
		self.TB = TabButton(self, self.group)

		#show
		self.webview.show()

	def do_then_init(self):

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
		self.group.set_title("RERows - " + title)
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

class Window(Garbbo.Window):
	def do_then_init(self):
		self.content = Tab(self).get()

if __name__ == "__main__":
	app = Window()
	Gtk.main()
