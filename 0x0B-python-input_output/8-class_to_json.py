#!/usr/bin/python3
"""Module for class to JSON conversion"""


def class_to_json(obj):
    """Returns dictionary description for JSON serialization of object"""
    return obj.__dict__