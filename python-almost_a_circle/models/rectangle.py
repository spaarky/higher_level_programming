#!/usr/bin/python3
"""
Module contains class Rectangle
Inherits from Base;
Inits superclass' id
Contains private width, height, x, y
"""


from models.base import Base


class Rectangle(Base):
    """
    defines class Rectangle; inherits from class Base
    Inherited Attributes:
        id
    Class Attributes:
        __width          __height
        __x              __y
    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
        update(self, *args, **kwargs)
        width(self)      width(self, value)
        height(self)     height(self, value)
        x(self)          x(self, value)
        y(self)          y(self, value)
        area(self)       display(self)
        __str__
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        getter width
        """
        return self.__width

    @property
    def height(self):
        """
        getter height
        """
        return self.__height

    @property
    def x(self):
        """
        getter x
        """
        return self.__x

    @property
    def y(self):
        """
        getter y
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        setter width
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """
        setter height
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        """
        setter x
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        """
        setter y
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """
        Return area
        """
        return self.__height * self.__width

    def display(self):
        """
        Print to stdout a rectangle using #'s
        """
        print('\n' * self.__y +
              '\n'.join(' ' * self.__x + '#' * self.__width
                        for index in range(self.__height)))

    def __str__(self):
        """
        Prints [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.__class__.__name__, self.id, self.__x, self.__y,
            self.__width, self.__height)

    def update(self, *args, **kwargs):
        """

        """
        if args:
            for index, value in enumerate(args):
                if index is 0:
                    self.id = value
                elif index is 1:
                    self.width = value
                elif index is 2:
                    self.height = value
                elif index == 3:
                    self.x = value
                else:
                    self.y = value
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """
        Return dictionary representation
        """
        dic = {}
        dic["id"] = self.id
        dic["width"] = self.width
        dic["height"] = self.height
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
