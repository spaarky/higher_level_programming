#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    if roman_string == '':
        return 0
    num = 0
    romanDic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for a, b in zip(roman_string, roman_string[1:]):
        if a not in romanDic.keys():
            return 0
        elif romanDic[a] >= romanDic[b]:
            num += romanDic[a]
        else:
            num -= romanDic[a]
    num += romanDic[roman_string[-1]]
    return num
