#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add as add, sub as sub, mul as mul, div as div
    import sys
    args = sys.argv
    arg_len = len(sys.argv) - 1
    table = {"+": add, "-": sub, "*": mul, "/": div}
    if arg_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if args[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(args[1])
    op = args[2]
    b = int(args[3])
    c = table[args[2]](a, b)
    print("{} {} {} = {}".format(a, op, b, c))


