import os

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

appname = "cRoWBaR"
version = "0.1.8"
comment = " Rethink Web BRowser"
home = "https://github.com/jeremi360/cRoWBaR"
icon = os.path.join(r, 'icons', 'icon.png')

authors = [
           "Jeremi 'jeremi360' Biernacki"
          ]