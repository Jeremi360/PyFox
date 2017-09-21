ChangeLog:
 - version 0.08.05:
	 - working restore closed tabs(still some bugs)
	 - now project use only svg icons
	 - fix prevoius url before page if finshed load
	 - fix none url when loading new page
	 - change broswer name to PyFox
	 - change grabbo in to PyGtkFX

 - version 0.07.21:
	 - fix About Dialog to fit new Grabbo.AboutDialog version
	 - remove gi.require_version('WebKit', '3.0') warning
	 - remove gi.require_version('Gtk', '3.0') warning
	 - better see tabs buttons now

 - version 0.07.19:
	 - small fix

 - version 0.07.18:
	 - fix About Dialog to fit new Grabbo.AboutDialog version
	 - now last history use "go-next" and "go-previous" icons

 - version 0.07.16:
	 - change all ".ui" files back to ".xml"

 - version 0.07.15:
	 - fix About Dialog to use new crowbar.getIcon Function
	 - remove wrong/unused import of Webkit2
	 - change size of logo on About Dialog License page to 32x32

 - version 0.07.12:
	 - all crowbar own icons default size is 16x16
	 - use new getIcon instead icons variables
	 - new icon for groups list button
	 - remove icons variables from crowbar
	 - add getIcon method to crowbar
	 - change search in url bar to Qwant

 - version 0.07.06:
	 - small fix

 - version 0.07.05:
	 - change all ".xml" files back to ".ui"
	 - fix About Dialog to fit new Grabbo.AboutDialog version

 - version 0.07.04:
	 - fix too big web page on Tabs
	 - fix too small scrolledwindow when is only 2 tabs
	 - add web page icon to title bar

 - version 0.07.02:
	 - Change Menu icon to cRoWBaR icon
	 - Use Grabbo.AboutDialog instead Gtk.AboutDialog
	 - DuckDuckGo search in url bar

 - version 0.06.02:
	 - rewrite tabs mechanic
	 - Don't show tabs until its more than 1
	 - Tabs on Top new good implementation using:
		 - Gtk.Notebook
		 - Gtk.RadioButton
		 - now selecting work correctly

 - version 0.05.00:
	 - very bad Tabs on Top implementation using:
	 	 - Gtk.Stack
	 	 - Gtk.StackSwitcher

 - version 0.04.00:
	 - Split to smallest files + make less imports

 - version 0.03.01:
	 - AboutDialog

 - version 0.03.00:
	 - Menu - only 3 bottom buttons work for now

 - version 0.02.00:
	 - history mini list(last history)

 - version 0.01.05:
	 - Full screen mode
	 - progress in url bar
	 - history back, forward buttons
	 - fix address mistake
	 - zoom in & out & and reset to 100%
	 - show web page
