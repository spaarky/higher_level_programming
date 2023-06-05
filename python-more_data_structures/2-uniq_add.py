#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list = list(dict.fromkeys(my_list))
    result = 0
    for index in my_list:
        result += index
    return result
