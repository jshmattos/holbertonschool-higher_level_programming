#!/bin/bash
# Sends a request to a URL and displays only the status code
curl -LI "$1" -o /dev/null -w '%{http_code}' -s
