#!/usr/bin/python3

"""
Module to check for shebang and documentation
requirements for Holberton Python assignments.

"""

import os
import importlib

if __name__ == '__main__':
    print()
    print("<---scanning local directory--->")
    print()
    shebang = '#!/usr/bin/python3'
    errors = 0

    files = []
    for file in sorted(os.listdir(os.getcwd())):
        if '.py' in file and not file.endswith('main.py'):
            o = open(file)
            first = o.readline()
            print("Checking {}...".format(file))
            if first.strip() == shebang:
                print("  Shebang - Good " + u'\u2713')
            else:
                errors += 1
                print("=============================")
                print("Incorrect shebang in {}".format(file))
                print("  '{}' should be '{}'".format(first.strip(), shebang))
                print("=============================")
                o.close()
                print()
                continue
            no_ext = file.replace(".py", "")
            tmp = importlib.import_module(no_ext)
            if tmp.__doc__ != None:
                print("  Module documentation - Good " + u'\u2713')
            else:
                errors += 1
                print("=============================")
                print("   Missing module documentation in {}!".format(file))
                print("=============================")
            di = no_ext.find('-')
            func = no_ext[di + 1:]
            try:
                if getattr(tmp, func).__doc__ != None:
                    print("  Function documentation - Good " + u'\u2713')
                else:
                    errors += 1
                    print("=============================")
                    print("   Missing function documentation in {}!".format(file))
                    print("=============================")
            except:
                pass
            finally:
                o.close()
                print()

    print("{:d} ERROR(S) FOUND".format(errors))

