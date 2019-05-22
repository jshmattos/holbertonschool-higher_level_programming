#!/usr/bin/python3

"""
This module contains the following functions:
    - lazy_matrix_mul

"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply 2 matrices by using the module NumPy.
    """
    x = np.array(m_a)
    y = np.array(m_b)
    return np.matmul(x, y)
