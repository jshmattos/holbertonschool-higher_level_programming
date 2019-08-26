#!/usr/bin/python3

"""
Takes in a string and sends a search request to the Star Wars API
"""

import pprint
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get("https://swapi.co/api/people/?search=" + argv[1])
    if "json" not in r.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        res = r.json()
        print("Number of results: " + str(res.get('count')))
        while True:
            search_res = res.get('results')
            for _ in search_res:
                print(_.get('name'))
            if res.get('next') is None:
                break
            else:
                res = requests.get(res.get('next')).json()
