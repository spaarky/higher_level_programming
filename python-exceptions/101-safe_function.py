#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except (ZeroDivisionError, ValueError, TypeError, IndexError) as msg:
        print('Exception {}'.format(msg), file=sys.stderr)
        return None
