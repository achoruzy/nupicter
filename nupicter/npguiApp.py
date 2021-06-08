#   Nupicter - Hand operated picture filtering tool
#   Copyright (C) 2021  Arkadiusz Choruzy
#
#   Arkadiusz Choruzy
#   achoruzy@gmail.com
import os
import filehandler as fh
import picture as npic
from PIL import Image
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.app import App
import kivy
kivy.require('2.0.0')


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class NupicterStartWidget(Widget):
    """App start GUI class."""

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(cancel=self.dismiss_popup, load=self.load)
        self._popup = Popup(title="Load picture file", content=content,
                            size_hint=(1, 1), background_color=(0.44, 0.62, 0.8))
        self._popup.open()

    def load(self, path, filename):
        file = fh.FileHandler(os.path.join(path, filename[0]))
        image = file.open()

        self.dismiss_popup()

        return print(image.as_array())


class NupicterApp(App):
    """App builder class."""

    def build(self):
        """Builder method - builds GUI."""
        return NupicterStartWidget()


if __name__ == '__main__':
    pass
