#!/usr/bin/python3

"""
Takes in a string and sends a search request to the Star Wars API
"""

import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    if "json" not in r.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        res = r.json()
        print(res.get('id'))
