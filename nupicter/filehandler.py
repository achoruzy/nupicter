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


class FileHandler():
    """Class for basic file operations."""

    def __init__(self, filepath: str):

        self.filepath = filepath

    def __exist__(self):
        pass

    def open(self):
        pass
