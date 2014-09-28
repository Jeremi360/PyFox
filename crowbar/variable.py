import os

def get_appdir():
    r = os.path.realpath(__file__)
    r = os.path.dirname(r)
    r = os.path.dirname(r)
    return r

appname = "cRoWBaR"
version = "0.2.2"
comment = "Rethinked Web BRowser"
home = "https://github.com/jeremi360/cRoWBaR"
rapport = "https://github.com/jeremi360/cRoWBaR/issues"
icon = os.path.join(get_appdir(), 'icons', 'icon.png')

authors = [
           "Jeremi 'jeremi360' Biernacki"
          ]