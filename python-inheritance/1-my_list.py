#!/usr/bin/python3
"""
Module 1-my_list
Contains class MyList
Inherits from list; has public instance method to print sorted
"""


class MyList(list):
    """
    Inherits from list

    methods:
        print_sorted(self)
    """
    def print_sorted(self):
        """
        prints list of ints all sorted in ascending order
        """
        print(sorted(self))
