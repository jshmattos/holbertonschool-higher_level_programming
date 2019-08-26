#!/usr/bin/python3

"""
Takes in a string and sends a search request to the Star Wars API
"""

import requests
from sys import argv

if __name__ == "__main__":
    github_commits = 'https://api.github.com/repos/'\
                     + argv[1] + '/' + argv[2] + '/commits'
    r = requests.get(github_commits)
    if "json" not in r.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        res = r.json()
        i = 0
        for r in res:
            if i > 9:
                break
            print(r.get('sha') + ': ', end="")
            print(r.get('commit').get('author').get('name'))
            i += 1
