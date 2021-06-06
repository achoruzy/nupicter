#   Nupicter - Hand operated picture filtering tool
#   Copyright (C) 2021  Arkadiusz Choruzy
#
#   Arkadiusz Choruzy
#   achoruzy@gmail.com
import os
import filehandler as fh
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

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        # with open(os.path.join(path, filename[0])) as stream:
        #     self.text_input.text = stream.read()
        file = fh.FileHandler(os.path.join(path, filename[0]))
        image = file.open()

        self.dismiss_popup()

        return image


class NupicterApp(App):

    def build(self):
        return NupicterStartWidget()


if __name__ == '__main__':
    pass
