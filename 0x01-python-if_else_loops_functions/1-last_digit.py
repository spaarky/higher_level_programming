#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# look for last digit
if number < 0:
    LastDigit = number % (-10)
else:
    LastDigit = number % 10

# print the output
if LastDigit > 5:
    print('Last digit of {} is {} and is greater than 5'.
          format(number, LastDigit))
elif LastDigit == 0:
    print('Last digit of {} is {} and is 0'.format(number, LastDigit))
else:
    print('Last digit of {} is {} and is less than 6 and not 0'
          .format(number, LastDigit))
