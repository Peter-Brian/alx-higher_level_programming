#!/usr/bin/python3
"""class Rectangle that defines a rectangle
    """


class Rectangle:
    """class rectangle
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """[summary]
        Keyword Arguments:
            width {int} -- [description] (default: {0})
            height {int} -- [description] (default: {0})
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """[summary]
        Returns:
            [type] -- [description]
        """
        return self.__width

    @width.setter
    def width(self, value):
        """[summary]
        Arguments:
            value {[type]} -- [description]
        Raises:
            TypeError: [width must be an integer]
            TypeError: [width must be >= 0]
        """
        if type(value) not in [int]:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """[summary]
        Returns:
            [type] -- [description]
        """
        return self.__height

    @height.setter
    def height(self, value):
        """[summary]
        Arguments:
            value {[type]} -- [description]
        Raises:
            TypeError: [height must be an integer]
            TypeError: [height must be >= 0]
        """
        if type(value) not in [int]:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """[summary]
        Returns:
            [type] -- [area]
        """
        return self.__width * self.__height

    def perimeter(self):
        """[summary]
        Returns:
            [type] -- [perimeter]
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """[summary]
        Returns:
            [type] -- [rectangle]
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        size = "#" * self.__width
        string = ""
        for i in range(self.__height):
            if i == self.__height - 1:
                string += size
            else:
                string += (size + "\n")
        return string

    def __repr__(self):
        """[summary]
        Returns:
            [type] -- [print widht anf hight]
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """[summary]
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
