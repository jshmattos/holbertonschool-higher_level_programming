#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that causes the server response
curl -L -H "Origin: HolbertonSchool" -X PUT -d "user_id=98" "$1"
