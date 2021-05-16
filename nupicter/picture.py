#   Nupicter - Hand operated picture filtering tool
#   Copyright (C) 2021  Arkadiusz Choruzy
#
#   Arkadiusz Choruzy
#   achoruzy@gmail.com

"""Nupicter's module for editing Picture objects created by FileHandler module.

Picture class handles objects converted to [[[R, G, B], [R, G, B], ...], ...] format
and includes methods for edition of such files.
"""


class Picture():

    def __init__(self, img):

        self.name = 'Picture Object'

        self.pixels = img


if __name__ == '__main__':
    pass
