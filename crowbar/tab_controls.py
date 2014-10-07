from gi.repository import Gtk
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import grabbo
import crowbar

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)


UI_TabC = os.path.join(r, 'ui', 'TabControls.xml')
class TabControls(grabbo.Builder):
	def __init__(self, mc, url = None):
		grabbo.Builder.__init__(self, UI_TabC)

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
		self.book = self.ui.get_object("book") #todo
		self.hist = self.ui.get_object("hist")
		self.ExtBox = self.ui.get_object("ExtBox") #todo
		self.fullb = self.ui.get_object("Full")
		self.ToolBox = self.ui.get_object("toolbox")
		self.RightScroll = self.ui.get_object("scrolledright")
		self.LeftScroll = self.ui.get_object("scrolledleft")
		self.TabsBox = self.ui.get_object("TabsBox")

		#findbox
		self.findbox = self.ui.get_object("findbox")
		self.findfb = self.ui.get_object("findfb")
		self.backfb = self.ui.get_object("backfb")
		self.nextfb = self.ui.get_object("nextfb")

		#this UI elements are hide until is not in use
		self.findbox.hide()
		self.RightScroll.hide()
		self.LeftScroll.hide()

		#create Notebook
		self.notebook = crowbar.Notebook(self, mc)
		self.TabsBox.pack_start(self.notebook, True, True, 1)
		self.notebook.show()

		#connect UI elements with methods

		#main tab toolbar
		self.back.connect("clicked", self.go_back)
		self.next.connect("clicked", self.go_next)
		self.fresh.connect("clicked", self.on_fresh)
		self.find.connect("toggled", self.on_findbox)
		self.zoomin.connect("clicked", self.zoom_in)
		self.zoomout.connect("clicked", self.zoom_out)
		self.zoomres.connect("clicked",  self.reset_zoom)
		self.fullb.connect("toggled", self.on_full)
		self.urlen.connect("activate", self.url_active)
		self.hist.connect("clicked", self.on_hist)

		#findbox
		self.findfb.connect("activate", self.on_find)
		self.backfb.connect("clicked", self.find_back)
		self.nextfb.connect("clicked", self.find_next)

		self.mc = mc

	def set_webview(self, wv):
		#connect WEBVIEW signals with methods
		self.webview = wv
		self.webview.connect("load-finished", self.finish_load)
		self.webview.connect("load-progress-changed", self.progress_load)

		self.webview.set_full_content_zoom(True)

		try:
			self.urlen.set_text(self.webview.get_uri())
		except:
			self.urlen.set_text("")

	def on_hist(self, button):
		if self.webview.can_go_forward() or self.webview.can_go_back():
			HList = Gtk.Popover.new(self.hist)
			box = Gtk.Box()
			box.set_orientation(Gtk.Orientation.VERTICAL)
			HList.add(box)

			fbl = self.webview.get_back_forward_list()

			if self.webview.can_go_forward():

				bl = fbl.get_forward_list_with_limit(5)

				for i in bl:
					self.HList_add(i, HList, box)

			if self.webview.can_go_back():

				bl = fbl.get_back_list_with_limit(5)

				for i in bl:
					self.HList_add(i, HList, box)

			HList.show_all()

	def HList_add(self, i, HList, box):
		s = crowbar.make_short(i.get_title(), 10)
		b = Gtk.Button(s)
		b.set_tooltip_text(i.get_title())
		img = Gtk.Image()
		b.set_image(img)

		try:
			pixbuf = self.webview.get_icon_pixbuf()
			b.get_image().set_from_pixbuf(pixbuf)
		except:
			b.get_image().set_from_icon_name("applications-internet")

		def on_button(button):
			s = self.make_short(i.get_uri())
			self.webview.load_uri(s)
			HList.hide()

		b.connect("clicked", on_button)
		box.add(b)

	def on_full(self, button):
		if self.fullb.get_active():
			self.mc.parent.fullscreen()
		else:
			self.mc.parent.unfullscreen()

	def get(self):
		return self.ui.get_object("box")

	def reset_zoom(self, button):
		self.webview.set_zoom_level(1.0)

	def go_back(self, button):
		self.webview.go_back()

	def go_next(self, button):
		self.webview.go_forward()

	def on_fresh(self, button):
		self.webview.reload()

	def zoom_in(self, button):
		self.webview.zoom_in()

	def zoom_out(self, button):
		self.webview.zoom_out()


	def on_find(self, widget):
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
			url = crowbar.defaultSearchEngine + url
		elif not "://" in url:
			url = "http://" + url

		self.webview.load_uri(url)

	def progress_load(self, webview, amount):
		self.urlen.set_progress_fraction(amount / 100.0)

	def finish_load(self, webview, frame):
		self.urlen.set_text(webview.get_uri())
		self.urlen.set_progress_fraction(0.0)

