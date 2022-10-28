#!/usr/bin/python3
""" JSON dude """
import json


def to_json_string(my_obj):
    """ json definition method
    Args:
        my_obj(str): passed object to represent
    Returns:
        The JSON representation of an object
    """
    return json.dumps(my_obj)
