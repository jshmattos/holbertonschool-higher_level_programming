#!/usr/bin/python3
def roman_to_int(roman_string):
    table = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100,
             'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9,
             'V': 5, 'IV': 4, 'I': 1}
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    prev, sum = 0, 0
    for c in roman_string:
        sum += table[c] if table[c] <= prev else table[c] - prev * 2
        prev = table[c]
    return sum
