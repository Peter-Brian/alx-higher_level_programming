#!/usr/bin/python3
""" class MyInt """


class MyInt(int):
    """ inherited from int """
    def __eq__(self, other):
        return int(self) != int(other)

    def __ne__(self, other):
        return int(self) == int(other)
