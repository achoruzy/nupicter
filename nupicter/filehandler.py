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
import PIL.Image

import nupicter.picture as nupp


class FileHandler():
    """FileHandler class to be use for basic file operations.

    As the main purpose, the class opens files and generates nupicter.Picture objects. 

    """

    def __init__(self, filepath: str):

        self.file = pathlib.Path(filepath)
        self.path = self.file.as_posix()

        self.exists = self.file.is_file()

    def _generate(self, img):
        """FileHandler method that returns a list of picture pixels. 

        For internal use only.

        Attributes:
            img (PIL.Image type object): Image object that going to be converted to pixel list.
        """

        width, height = img.size
        pixels = img.load()

        pixel_list = []
        for h in range(height):
            width_list = []

            for w in range(width):
                pix = pixels[w, h]
                width_list.append(pix)

            pixel_list.append(width_list)

        return pixel_list

    def open(self):
        """FileHandler method for open picture file and generate nupicter.Picture object.

        Returns:
            An nupicter.Picture object
        """
        if self.exists:
            img = PIL.Image.open(self.path)
            pixel_list = self._generate(img)
            return nupp.Picture(pixel_list)
