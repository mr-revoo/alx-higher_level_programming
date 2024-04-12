#!/usr/bin/python3

"""
    This module contains function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
        matrix_divided - divides all elements of a matrix.
        Args:
            matrix (list): first parameter (the matrix)
            div (int): second parameter (the divisor)
        Returns:
            list: the matrix with all elements divided
    """
    e_m_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(e_m_msg)
    for x in matrix:
        if type(x) is not list:
            raise TypeError(e_m_msg)
        for i in x:
            if type(i) is not int and type(i) is not float:
                raise TypeError(e_m_msg)
        if len(x) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(column / div, 2) for column in row] for row in matrix]
