#!/usr/bin/python3
"""Module for lookup method."""


def lookup(obj):
    """Returns list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        List of attributes and methods.
    """
    return dir(obj)