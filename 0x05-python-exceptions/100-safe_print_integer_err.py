import sys


def safe_print_integer_err(value):
    is_int = True
    try:
        print("{:d}".format(value))
    except ValueError:
        sys.stderr.write(
            "Exception: Unknown format code 'd' for object of type ")
        if isinstance(value, str):
            sys.stderr.write("'str'\n")
        elif isinstance(value, float):
            sys.stderr.write("'float'\n")
        is_int = False
    return is_int
