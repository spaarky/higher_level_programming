#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length > 0:
        letter = sentence[0]
    else:
        return None

    return (length, letter)
