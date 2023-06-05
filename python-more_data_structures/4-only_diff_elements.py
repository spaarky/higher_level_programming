#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diffs1 = list(set(set_1) - set(set_2))
    diffs2 = list(set(set_2) - set(set_1))
    diffs = diffs1 + diffs2
    return diffs
