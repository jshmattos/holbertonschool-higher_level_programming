#!/usr/bin/python3

"""
This module contains the following functions:
    - lazy_matrix_mul

"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply 2 matrices using the module NumPy.
    """
    return np.matmul(m_a, m_b)
