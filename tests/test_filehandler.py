#   Nupicter - Hand operated picture filtering tool
#   Copyright (C) 2021  Arkadiusz Choruzy
#
#   Arkadiusz Choruzy
#   achoruzy@gmail.com


import nupicter.filehandler as nupf

FILEPATHS = {'png': 'testfiles\\filehandler_png_1.png'}


class TestFileHandler():

    def test_class(self):
        fh = nupf.FileHandler(FILEPATHS['png'])

        assert type(fh) == nupf.FileHandler

    def test_open(self):
        fh = nupf.FileHandler(FILEPATHS['png'])
        result = fh.open()

        assert type(result) == nupf.FileHandler
