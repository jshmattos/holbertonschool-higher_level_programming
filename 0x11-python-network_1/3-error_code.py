#!/usr/bin/python3

"""
Takes in a URL, sends a request to the URL and displays the body of
the response (decoded in utf-8).
"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as f:
            print(f.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        error_code = str(e).split(' ')[2][:-1]
        print("Error code: " + str(error_code))
