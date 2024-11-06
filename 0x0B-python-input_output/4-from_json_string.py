#!/usr/bin/python3
"""Module for JSON string to object conversion"""
import json


def from_json_string(my_str):
    """Returns object represented by a JSON string"""
    return json.loads(my_str)