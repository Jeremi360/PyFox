from gi.repository import Gtk
from grabbo import Builder
import os

ExtBox_UI = os.path.join('..', 'ui', 'ExtBox.ui')

class ExtBox(Builder):
    def __init__(self, ext):
        super(ExtBox, self).__init__(ExtBox_UI)


class Extension(object):
    def __init__(self, Name, Descrption, Author, url, Icon):
        self._name = Name
        self._des = Descrption
        self._aur = Author
        self._url = url
        self._icon = Icon

        self._box =

        self._

