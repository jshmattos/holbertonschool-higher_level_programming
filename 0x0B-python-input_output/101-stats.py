#!/usr/bin/python3

import sys
import signal
from time import sleep

file_size = 0
stats = {
    "file_size": 0,
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0}
counter = 0


def print_stats(stats: dict) -> None:
    print("File size: {}".format(file_size))
    stat_arr = sorted(stats.keys())
    for num in stat_arr:
        if stats[num]:
            print(str(num) + ": " + str(stats[num]))

try:
    for line in sys.stdin:
        counter += 1
        data = line.split()
        status_code = data[7]
        stats[status_code] += 1
        file_size += int(data[8])
        if counter % 10 == 0:
            print_stats(stats)
except KeyboardInterrupt:
    print_stats(stats)
    raise
