import os

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

appname = "cRoWBaR"
version = "0.05"
comment = "Rethinked Web BRowser"
home = "https://github.com/jeremi360/cRoWBaR"
rapport = "https://github.com/jeremi360/cRoWBaR/issues"
icon = os.path.join(r, 'icons', 'icon.png')
svgicon = os.path.join(r, 'icons', 'icon.svg')
licensetxt = os.path.join(r, 'LICENSE')
defaultSearchEngine = "https://duckduckgo.com/?q="

abouttxt = "Program and designed by Jeremi 'jeremi360' Biernacki"

TabSwitcherSize = 265