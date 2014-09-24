![Logo][5] **cRoWBaR** - Rethink Web BRowser

Icon/Logo based on *Vinegard* icon from icon theme [*Faenza* by tiheum][6]

Screenshot:
![cRoWBaR in Action][1]

**cRowBaR** is simple web browser for Linux inspired by:

 *  Firefox:
    * Aurialis UI
    * Paronama
    * Addons:

        * BackToTop
        * FlashBlock
        * AddToSearchBar
        * UndoTab
        * AdBlock
        * OpenWith

 * Google Chrome - ominbox
 * Opera 12 Addons

If you won to compile/run this you will need:

- [python version 3.x][2]
- Gtk(3.12 or higher) and Webkit from gi repository:

	- Linux see your dist repo
	- Windows download [from hear][3]

- My [Grabbo lib][4]

To run just double click on main.py in corwbar folder.

version: 0.2.2
"Warning: This program is not finished"

Done:

* Split to smallest files + make less imports
* AboutDialog
* Menu - only 3 bottom buttons work for now
* history mini list
* Full screen mode
* Tabs on Top - now on title bar:
	 - rewrite using Gtk.Stock and Gtk.StockSwitcher
	 - fixed!
	 - like dock!
	 - use RadioButtons

* google search in url bar
* progress in url bar
* history back, forward buttons
* fix address mistake
* zoom in & out & and reset to 100%
* show favicon

ToDo:

* menu
* History browsing
* Bookmarks
* new tab page
* connect open in new tab with addtab
* Addons(they are planed for 2.x version)
* Paronoma as list
* Downloads
* Settings
* restore previous session



[1]:https://raw.githubusercontent.com/jeremi360/cRoWBaR/master/shot.png
[2]:https://www.python.org/
[3]:http://sourceforge.net/projects/pygobjectwin32/files/
[4]:https://github.com/jeremi360/Grabbo
[5]:https://raw.githubusercontent.com/jeremi360/cRoWBaR/master/icons/icon.png
[6]:http://tiheum.deviantart.com/art/Faenza-Icons-173323228
