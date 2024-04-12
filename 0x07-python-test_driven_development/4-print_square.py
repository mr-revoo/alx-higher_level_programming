#!/usr/bin/python3

"""
    This module contains function that prints a square with the character #.
"""


def print_square(size):
    """
        print_square - prints a square with the character #.
        Args:
            size (int): size length of the square.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
