#   Nupicter - Hand operated picture filtering tool
#   Copyright (C) 2021  Arkadiusz Choruzy
#
#   Arkadiusz Choruzy
#   achoruzy@gmail.com

"""Nupicter's module for handling and operating files.

The basic FileHandler class can open a graphics file and
handle all the file operations on it. It's purpose is also
to create a data object for later operations."""

import pathlib
import PIL

import nupicter.picture as nupp


class FileHandler():
    """Class for basic file operations."""

    def __init__(self, filepath: str):

        self.file = pathlib.Path(filepath)

        self.path = self.file.as_posix()

        self.exists = self.file.is_file()

    def open(self):
        if self.exists:
            with open(self.path, mode='r') as img:
                editable_img = self.generate(img)
                return nupp.Picture(editable_img)

    def generate(self, img):
        return 'test'
