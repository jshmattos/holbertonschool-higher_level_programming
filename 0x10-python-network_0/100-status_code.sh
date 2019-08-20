#!/bin/bash
# Sends a request to a URL and displays only the status code
curl -s -L -I "$1" -o /dev/null -w '%{http_code}'
