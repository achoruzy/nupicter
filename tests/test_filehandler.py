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
    'png': 'C:/Users/achor/Desktop/Python/Projects/002_Nupicter/tests/testfiles/filehandler_png_1.png'}
IN_USE = 'png'


class TestFileHandler():

    def test_class(self):
        fh = nupf.FileHandler(FILEPATHS[IN_USE])

        assert type(fh) == nupf.FileHandler

    def test__init__(self):
        fh = nupf.FileHandler(FILEPATHS[IN_USE])

        if platform.system() == 'Windows':
            assert type(fh.file) == pathlib.WindowsPath
        elif platform.system() == 'Linux':
            assert type(fh.file) == pathlib.PosixPath

        testfile = fh.file

        assert testfile.suffix == '.png'
        assert testfile.name == 'filehandler_png_1.png'

        assert fh.exists == True

    def test_open(self):
        fh = nupf.FileHandler(FILEPATHS[IN_USE])
        result = fh.open()

        assert type(result) == nupp.Picture
