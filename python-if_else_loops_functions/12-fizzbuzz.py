#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        # modulo 3 et modulo 5 reviennent a avoir modulo 15
        if number % 15 == 0:
            print('FizzBuzz ', end='')
        elif number % 3 == 0:
            print('Fizz ', end='')
        elif number % 5 == 0:
            print('Buzz ', end='')
        else:
            print('{} '.format(number), end='')
