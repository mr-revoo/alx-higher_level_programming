#!/usr/bin/python3

"""
    This module contains function that add two integers.
"""


def add_integer(a, b=98):
    """
        add_integer - adds two integers
        Args:
            a (int): first integer
            b (int): second integer
        Returns:
            int: sum of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
