#!/usr/bin/python3

"""
Takes in a string and sends a search request to the Star Wars API
"""

import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get("https://swapi.co/api/people/?search=" + argv[1])
    if "json" not in r.headers['content-type']:
        print("Not a valid JSON")
    else:
        res = r.json()
        print("Number of results: " + str(res.get('count')))
        for r in res['results']:
            print(r.get('name'))
