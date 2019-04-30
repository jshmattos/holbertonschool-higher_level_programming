#!/usr/bin/python3
def uppercase(str):
    res = ""
    for c in str:
        if ord(c) in range(97, 123):
            res += chr(ord(c) - 32)
        else:
            res += c
    print("{}".format(res))
