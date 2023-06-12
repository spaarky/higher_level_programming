#!/usr/bin/python3
"""
Module 1-square
Define class Square with private attribute size
"""


class Square:
    """
    class Square definition

    Args:
        size: size of a side of the square
    """
    def __init__(self, size):
        """
        Initialize square

        Attribute:
            size: size of a side in the square
        """
        self.__size = size
