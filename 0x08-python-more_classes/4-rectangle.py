#!/usr/bin/python3
"""This module contain the rectangle class."""


class Rectangle:
    """Empty class Rectangle that defines a rectangle."""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return (self.height * self.width)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.height + self.width) * 2)

    def __str__(self):
        if not self.width or not self.height:
            return ""
        return((('#' * self.width) + '\n') * self.height)[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
