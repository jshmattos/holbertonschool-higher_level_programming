#!/usr/bin/python3


def safe_print_integer(value):
    is_int = True
    try:
        print("{:d}".format(value))
    except BaseException:
        is_int = False
    return is_int
