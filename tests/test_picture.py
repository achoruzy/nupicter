#   Nupicter - Hand operated picture filtering tool
#   Copyright (C) 2021  Arkadiusz Choruzy
#
#   Arkadiusz Choruzy
#   achoruzy@gmail.com


import nupicter.filehandler as nupf
import nupicter.picture as nupp

import numpy as np

FILEPATHS = {
    'png': 'C:/Users/achor/Desktop/Python/Projects/002_Nupicter/tests/testfiles/4by4.png'}
IN_USE = 'png'

file = nupf.FileHandler(FILEPATHS[IN_USE])


class TestPicture():

    def test_init(self):
        """ Tests class __init__ . """

        pic = file.open()

        assert type(pic.pixels) == list
        assert pic.pixels[0][0] == [237, 28, 36]

    def test_as_array(self):
        pic = file.open()

        pix_array = pic.as_array()

        assert type(pix_array) == np.ndarray
        assert list(pix_array[0][0]) == [237, 28, 36]

    def test_return_picture(self):
        pic = file.open()

        new_picture_obj = pic.return_picture()

        assert type(new_picture_obj) == nupp.Picture


if __name__ == '__main__':
    # pass

    from PIL import Image
    import numpy as np

    im = Image.open(FILEPATHS[IN_USE])
    a = np.asarray(im)

    img = Image.fromarray(a)

    print(a[0][0])
