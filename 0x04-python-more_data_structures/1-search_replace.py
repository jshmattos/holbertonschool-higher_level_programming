#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if x == 2 else x for x in my_list]
