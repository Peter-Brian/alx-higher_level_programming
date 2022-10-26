#!/usr/bin/python3
"""Module for number_of_lines function."""


def number_of_lines(filename=""):
    """This function return the number of lines of a text file."""
    with open(filename) as f:
        total = 0
        for run in enumerate(f):
            total = total + 1
    return total
