#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortedDict = dict(sorted(a_dictionary.items()))
    for a, b in sortedDict.items():
        print('{}: {}'.format(a, b))
