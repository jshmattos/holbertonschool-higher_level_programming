#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in row:
            print("{:d}".format(i), end=" " if row[-1] != i else "")
        print()

# print('\n'.join([''.join(
#       [str(i) + " " for i in row]).strip() for row in matrix]))
