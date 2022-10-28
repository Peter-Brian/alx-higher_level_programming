#!/usr/bin/python3
""" new class in here inherited from rectangle """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class inherited from Rectangle """
    def __init__(self, size):
        """ initialization
        Args:
            size (int)
    """
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        """ area implementation """
        return self.__size * self.__size

    def __str__(self):
        """ method definition """
        return "[Square] {}/{}".format(self.__size, self.__size)
