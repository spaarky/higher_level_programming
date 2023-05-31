#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == '__main__':
    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    operator = argv[2]
    function = {"+": add, "-": sub, "*": mul, "/": div}
    if operator not in function:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    print('{:d} {:s} {:d} = {:d}'.format(a, operator, b, function[operator](a, b)))
