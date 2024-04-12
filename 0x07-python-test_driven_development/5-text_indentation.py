#!/usr/bin/python3

"""
    This module contains function that prints a text with 2 new lines
    after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
        text_indentation - prints a text with 2 new lines
        after each of these characters: ., ? and :
        Args:
            text (str): text to print.
    """
    new_line = False
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i])
            print()
            new_line = True
        else:
            if text[i] == ' ' and new_line is True:
                continue
            else:
                print(text[i], end='')
            new_line = False
