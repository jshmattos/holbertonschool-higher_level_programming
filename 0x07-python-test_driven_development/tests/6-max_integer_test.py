#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test for max integer."""

    def test_empty_list(self):
        """Test for empty list."""
        self.assertEqual(max_integer(), None)

    def test_valid_input(self):
        """Test with valid input."""
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([-1, -5, -4, 0]), 0)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([100]), 100)
        self.assertEqual(max_integer([429509, 3424, -1]), 429509)

if __name__ == '__main__':
        unittest.main()