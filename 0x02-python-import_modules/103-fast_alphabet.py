#!/usr/bin/python3
from functools import reduce
arr = print(reduce(lambda a, b: a + b,
                   [chr(x) for x in range(ord('A'), ord('Z') + 1)], ""))
