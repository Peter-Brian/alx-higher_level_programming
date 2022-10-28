#!/usr/bin/python3
""" method that creates an object from a json file """
import json


def load_from_json_file(filename):
    """ json method definition creates an object from json file """
    with open(filename, encoding='utf-8') as file:
        return json.load(file)
