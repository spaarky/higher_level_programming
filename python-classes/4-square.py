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
            size (int): defaults to 0 if None
        """
        self.size = size

    @property
    def size(self):
        """
        Getter

        Returns:
            size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter

        Args:
            value: set size of side, if int and >= 0
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
