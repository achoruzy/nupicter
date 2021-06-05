#   Nupicter - Hand operated picture filtering tool
#   Copyright (C) 2021  Arkadiusz Choruzy
#
#   Arkadiusz Choruzy
#   achoruzy@gmail.com

from kivy.uix.widget import Widget
from kivy.app import App
import kivy
kivy.require('2.0.0')


class NupicterWidget(Widget):
    pass


class NupicterApp(App):

    def build(self):
        return NupicterWidget()


if __name__ == '__main__':
    pass
