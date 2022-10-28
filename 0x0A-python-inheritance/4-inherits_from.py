#!/usr/bin/python3
"""Module for inherits_from method."""


def inherits_from(obj, a_class):
    """
    This method determines if the object is a true subclass from
    the specified class.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
