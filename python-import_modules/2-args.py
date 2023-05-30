if __name__ == "__main__":
    from sys import argv
    userin = argv[1:]
    size = len(userin)
    print('{:d} {:s}{:s}'.
          format(size,
                  'arguments' if (size) is not 1 else 'argument',
                  '.' if (size) is 0 else ':'))
    for index, arg in enumerate(userin):
        print('{:d}: {:s}'.format(index + 1, arg))
