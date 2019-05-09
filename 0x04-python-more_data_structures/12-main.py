#!/usr/bin/python3
""" Roman to Integer test file
"""
from time import time

roman_to_int = __import__('12-roman_to_int').roman_to_int

start = time()
roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
end = time()
print(end - start)

start = time()
roman_number = "VVV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
end = time()
print(end - start)

start = time()
roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
end = time()
print(end - start)

start = time()
roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
end = time()
print(end - start)

start = time()
roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
end = time()
print(end - start)
