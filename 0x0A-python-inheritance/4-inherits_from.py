#!/usr/bin/python3
"""Module for inherits_from method."""


def inherits_from(obj, a_class):
    """Check if object is an instance of a class inherited from specified class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.

    Returns:
        True if obj inherits from a_class, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class