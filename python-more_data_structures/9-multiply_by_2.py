#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict = {}
    tmp = {}
    if a_dictionary is not None:
        for key, value in a_dictionary.items():
            newValue = value * 2
            tmp = {key: newValue}
            dict.update(tmp)
        return dict
    return None
