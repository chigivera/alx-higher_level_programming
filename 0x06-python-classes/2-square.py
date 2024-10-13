#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """
    This class defines a square.
    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size