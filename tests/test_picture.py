#   Nupicter - Hand operated picture filtering tool
#   Copyright (C) 2021  Arkadiusz Choruzy
#
#   Arkadiusz Choruzy
#   achoruzy@gmail.com


import nupicter.filehandler as nupf
import nupicter.picture as nupp

import pathlib
import os
import sys
import platform

FILEPATHS = {
    'png': 'C:/Users/achor/Desktop/Python/Projects/002_Nupicter/tests/testfiles/4by4.png'}
IN_USE = 'png'

file = nupf.FileHandler(FILEPATHS[IN_USE])


class TestPicture():

    def test_print(self):
        """ Tests __str__ method. """

        pic = file.open()

        assert type(pic.pixels) == list
        assert pic.pixels[0][0] == (237, 28, 36)


if __name__ == '__main__':
    pass
    # tp = file.open()

    # print(tp.name)

    # tp_list = tp

    # print(tp_list)
