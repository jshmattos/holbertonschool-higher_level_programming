#!/usr/bin/python3

"""
Takes in a string and sends a search request to the Star Wars API
"""

import requests
from sys import argv

if __name__ == "__main__":
    s = requests.session()
    r = s.get("https://swapi.co/api/people/?search=" + argv[1])
    if "json" not in r.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        res = r.json()
        print("Number of results: " + str(res.get('count')))
        while True:
            search_res = res.get('results')
            for _ in search_res:
                print(_.get('name'))
                if _.get('films'):
                    for film in _.get('films'):
                        f = s.get(film).json()
                        print("\t" + f.get('title'))
            if res.get('next') is None:
                break
            else:
                res = s.get(res.get('next')).json()
