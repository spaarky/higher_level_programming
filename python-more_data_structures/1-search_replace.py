#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is not None:
        return ([list if list is not search else replace for list in my_list])
    return None
