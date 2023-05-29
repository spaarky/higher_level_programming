#!/usr/bin/python3
for index in range(ord('z'), ord('a')-1, -1):
    print('{:c}'.format(index) if index % 2 == 0 else chr(index-32), end='')
    # relation in ASCII between lower and uppercase letters (-32 of index)
