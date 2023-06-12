#!/usr/bin/python3
"""
Module 1-square
Define class Square with private attribute size and validate size
"""


class Square:
    """
    class Square definition

    Args:
        size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """
        Initialize square

        Attribute:
            __size (int): size of a side in the square, defaults to 0 if None
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
