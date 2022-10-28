#!/usr/bin/python3
""" class BaseGeometry with public instance method """


class BaseGeometry:
    """ BaseGeometry class """
    def area(self):
        """ area method definition
        Raises:
            Exception: when area is not implemented
        """
        raise Exception("area() is not implemented")
