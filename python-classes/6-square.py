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

    Functions:
        __init__(self, size)
        def size(self)
        def size(self, value)
        def position(self)
        def position(self, value)
        area(self)
        def my_print(self)
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize square

        Attribute:
            size (int): defaults to 0 if None
        """
        self.size = size
        self.position = position

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

        Attribute:
            value: sets size of value, 0 if None
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """
        Getter

        Returns:
            position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter

        Attribute:
            value: sets position to value if tuple is 2 integers ints
        """
        if type(value) is not tuple or len(value) is not 2 or type(value[0]) is not int or type(value[1]) is not int or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value


    def area(self):
        """
        Calculation of area of square

        Returns:
            area
        """
        return (self.__size)**2

    def my_print(self):
        """
        print square with '#'
        """
        print('\n'.join(['#' * self.__size for rows in range(self.__size)]))
