from gi.repository import Gtk
from grabbo import Builder
import os

ExtBox_UI = os.path.join('..', 'ui', 'ExtBox.ui')

class Extension(object):
    def __init__(self, Name, Descrption, Author, url, Icon):
        self._name = Name
        self._des = Descrption
        self._aur = Author
        self._url = url
        self._icon = Icon

    def get_name(self):
        return self._name

    def get_descrption(self):
        return self._des

    def get_author(self):
        return self._aur

    def get_url(self):
        return self._url

    def get_icon(self):
        return self._icon


class ExtBox(Builder):
    def __init__(self, ext = Extension):
        super(ExtBox, self).__init__(ExtBox_UI)
        self._label = self.ui.get_object("label")
        self._icon = self.ui.get_object("image")
        self._switch = self.ui.get_object("switch")
        self._text = self.ui.get_object("textview")

        self._label Gtk.Label.set_text(ext.)




