#!/usr/bin/python3

"""
Fetches https://intranet.hbtn.io/status
"""

import requests

if __name__ == "__main__":
    response = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("    - type: {}".format(type(response.text)))
    print("    - content: {}".format(response.text))
