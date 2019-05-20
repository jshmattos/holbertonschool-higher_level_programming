def safe_print_division(a, b):
    try:
        prod = a / b
    except ZeroDivisionError:
        prod = None
    finally:
        print("Inside result: {}".format(prod))
    return prod
