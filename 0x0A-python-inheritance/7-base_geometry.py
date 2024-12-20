#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Method to compute area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name: The name of the parameter.
            value: The parameter to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))