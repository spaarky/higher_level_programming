#!/usr/bin/python3
"""
Module 5-to_json_string
Contains function that returns JSON representation of obj (string)
"""


def to_json_string(my_obj):
    """
    Args:
        my_obj: python object

    Returns:
        JSON representation of obj (string)
    """
    import json

    return (json.dumps(my_obj))
