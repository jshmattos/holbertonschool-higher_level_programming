#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    print('\n'.format().join(
        [''.join([str(i) + " " for i in row]).strip() for row in matrix]))
