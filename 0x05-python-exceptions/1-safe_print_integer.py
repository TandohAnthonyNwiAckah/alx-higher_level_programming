#!/usr/bin/python3
def safe_print_integer(value):
    checkBool = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        checkBool = False
    return checkBool
