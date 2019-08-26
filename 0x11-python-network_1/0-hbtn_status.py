#!/usr/bin/python3

"""
Fetches https://intranet.hbtn.io/status
"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as f:
        r = f.read()
        print("Body response:")
        print("    - type: {}".format(type(r)))
        print("    - content: {}".format(r))
        print("    - utf8 content: {}".format(r.decode('utf-8')))
