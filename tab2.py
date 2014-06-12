# forked from https://gist.github.com/kklimonda/890640
# by Jeremi "jeremi360" Biernacki


from gi.repository import Gtk
import os

UI_tab = os.path.join("ui", "Tab.ui")

class Tab(object):
	def __init__(self):
		self.ui = Gtk.Builder()
		self.ui.add_from_file(UI_tab)
		self.ui.connect_signals(self)

if __name__ == "__main__":
	app = Tab()
	Gtk.main()
