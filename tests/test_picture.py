#   Nupicter - Hand operated picture filtering tool
#   Copyright (C) 2021  Arkadiusz Choruzy
#
#   Arkadiusz Choruzy
#   achoruzy@gmail.com


import nupicter.filehandler as nupf
import nupicter.picture as nupp

import numpy as np

import pytest


FILEPATHS = {
    'png': 'C:/Users/achor/Desktop/Python/Projects/002_Nupicter/tests/testfiles/4by4.png'}
IN_USE = 'png'

file = nupf.FileHandler(FILEPATHS[IN_USE])


class TestPicture():

    def test_init(self):
        """Tests if class __init__ works properly and Picture object is well built."""

        pic = file.open()

        assert type(pic.pixels) == list
        assert pic.pixels[0][0] == [237, 28, 36]

    def test_as_array(self):
        """Tests if Picture.as_arraty returns proper numpy.array object."""

        pic = file.open()
        pix_array = pic.as_array()

        assert type(pix_array) == np.ndarray
        assert pix_array.shape == (4, 4, 3)
        assert list(pix_array[0][0]) == [237, 28, 36]

    def test_return_picture(self):
        """Tests if Picture.return_picture creates proper Picture object."""

        pic = file.open()
        new_picture_obj = pic.return_picture()

        assert type(new_picture_obj) == nupp.Picture

    def test_save_exception(self):
        """Tests exceptions that may occure when Picture.save is used.
        If all exception tests are handled in test then file creation will work."""

        pic = file.open()
        path = 'C:/Users/achor/Desktop/Python/Projects/002_Nupicter/tests/testfiles/'

        with pytest.raises(Exception):
            assert pic.save('something', 'filename')

        with pytest.raises(Exception):
            assert pic.save(path, '$%^aaaaaa_')

        with pytest.raises(Exception):
            assert pic.save(path, 'savetest', 'XYz')

    def test_grayscale(self):
        """Tests if Picture.grayscale method creates proper data."""

        pic = file.open()

        gs_test = pic.grayscale()

        assert type(pic.pixels) == list
        assert pic.pixels[0][0] == [73, 73, 73]

    def test_grayscale_coef(self):
        """Tests if Picture.grayscale method properly works with hand input grayscale coefficient."""

        pic_coe = file.open()

        gs_test = pic_coe.grayscale(coef=(0.25, 0.8, 0.13))

        assert pic_coe.pixels[0][0] == [86, 86, 86]


if __name__ == '__main__':
    pass
