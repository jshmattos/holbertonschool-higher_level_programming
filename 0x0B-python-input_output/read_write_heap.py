#!/usr/bin/python3

'''
This is a module for read_write_heap.py.
Sources:
    https://blog.holbertonschool.com/hack-the-virtual-memory-c-strings-proc/
    Thanks Julien Barbier!
'''

import sys

if len(sys.argv) != 4:
    sys.stderr.write("Usage: <pid> <search_string> <replace_string>\n")
    sys.exit(1)

pid = sys.argv[1]
search_string = sys.argv[2]
write_string = sys.argv[3]

# open the maps and mem files of the process
maps = "/proc/" + pid + "/maps"
print("[*] maps: {}".format(maps))
mem = "/proc/" + pid + "/mem"
print("[*] mem: {}".format(mem))

# try opening the maps file
try:
    with open(maps, "r") as maps_f:
        for line in maps_f:
            # check if we found the heap
            if "[heap]" in line:
                print("[*] Found [heap]:")

            # check if there is read and write permission
                if 'r' not in line or 'w' not in line:
                    print("[*] {} does not have read/write permission".format(maps))
                    sys.exit(0)

                sline = line.split(' ')

                # parse line
                addr = sline[0]
                perm = sline[1]
                offset = sline[2]
                device = sline[3]
                inode = sline[4]
                pathname = sline[-1][:-1]
                print("\tpathname = {}".format(maps))
                print("\taddresses = {}".format(addr))
                print("\tpermisions = {}".format(perm))
                print("\toffset = {}".format(offset))
                print("\tinode = {}".format(inode))

                # get start and end of the heap in the virtual memory
                addr = addr.split("-")
                if len(addr) != 2:  # never trust anyone, not even your OS :)
                    print("[*] Wrong addr format")
                    sys.exit(1)
                addr_start = int(addr[0], 16)
                addr_end = int(addr[1], 16)
                print("\tAddr start [{:x}] | end [{:x}]".format(addr_start, addr_end))

except IOError as e:
    print("[ERROR] Can not open file {}:".format(maps))
    print("        I/O error({}): {}".format(e.errno, e.strerror))
    sys.exit(1)

# open and read mem
try:
    with open(mem, 'rb+') as mem_file:
        # read heap
        mem_file.seek(addr_start)
        heap = mem_file.read(addr_end - addr_start)

        # find string
        try:
            i = heap.index(bytes(search_string, "ASCII"))
        except Exception:
            print("Can't find '{}'".format(search_string))
            sys.exit(0)
        print("[*] Found '{}' at {:x}".format(search_string, i))

        # write the new string
        print("[*] Writing '{}' at {:x}".format(write_string + '\0', addr_start + i))
        mem_file.seek(addr_start + i)
        mem_file.write(bytes(write_string, "ASCII"))

except IOError as e:
        print("[ERROR] Can not open file {}:".format(mem_filename))
        print("        I/O error({}): {}".format(e.errno, e.strerror))
        sys.exit(1)
