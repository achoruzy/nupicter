#   Nupicter - Hand operated picture filtering tool
#   Copyright (C) 2021  Arkadiusz Choruzy
#
#   Arkadiusz Choruzy
#   achoruzy@gmail.com

"""Working test for checking proper behaviour of basic application workflow.

Working steps:
    1. Open coloured test file
    2. Create Picture object
    3. Edit the object using grayscale method
    4. Save the object to the file

Returned file should be entirely grayscale and possible to open.
"""

import nupicter.filehandler as nupf
import nupicter.picture as nupp

if __name__ == '__main__':
    FILEPATHS = {
        'png': 'C:/Users/achor/Desktop/Python/Projects/002_Nupicter/tests/testfiles/4by4.png'}
    IN_USE = 'png'

    file = nupf.FileHandler(FILEPATHS[IN_USE])

    pic = file.open()

    pic.grayscale()

    save_path = 'C:/Users/achor/Desktop/Python/Projects/002_Nupicter/tests/testfiles/'
    save_file = 'worktest_picture_bw_save'

    pic.save(save_path, save_file)
