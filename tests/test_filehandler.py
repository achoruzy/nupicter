#   Nupicter - Hand operated picture filtering tool
#   Copyright (C) 2021  Arkadiusz Choruzy
#
#   Arkadiusz Choruzy
#   achoruzy@gmail.com

import nupicter as nupf


class test_FileHandler():

    fh = nupf.FileHandler()

    def test_open():
        fh.open()
