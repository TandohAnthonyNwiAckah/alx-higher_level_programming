#!/usr/bin/python3
"""
    0-add_integer.py module
    Contains the function add_integer
    Returns the sum of parameters. Example:
    >>>add_integer(10, 4)
    14
"""


def add_integer(a, b=98):
    """
        adds two integer | float values
        args:
            a(int | float): parameter 1
            b(int | float): parameter  2
        returns the sum
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
