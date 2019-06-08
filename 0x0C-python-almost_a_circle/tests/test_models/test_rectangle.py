#!/usr/bin/python3

"""
Unittest for models/rectangle.py
"""

import unittest
from models.rectangle import Rectangle

class RectangleTest(unittest.TestCase):
    """Tests for rectangle class."""

    def test_00_one_arg(self):
        """Test for one argument passed in."""
        with self.assertRaises(TypeError) as x:
            r0 = Rectangle(5)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'",
            str(x.exception))

    def test_01_two_args(self):
        """Test for two arguments passed in."""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_02_three_args(self):
        """Test for three arguments passed in."""
        r2 = Rectangle(98, 12, 64)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 98)
        self.assertEqual(r2.height, 12)
        self.assertEqual(r2.x, 64)
        self.assertEqual(r2.y, 0)

    def test_03_four_args(self):
        """Test for four arguments passed in."""
        r3 = Rectangle(4, 51, 96, 88)
        self.assertEqual(r3.id, 3)
        self.assertEqual(r3.width, 4)
        self.assertEqual(r3.height, 51)
        self.assertEqual(r3.x, 96)
        self.assertEqual(r3.y, 88)

    def test_04_five_args(self):
        """Test for five arguments passed in."""
        r4 = Rectangle(5, 66, 151, 44, 822)
        self.assertEqual(r4.id, 822)
        self.assertEqual(r4.width, 5)
        self.assertEqual(r4.height, 66)
        self.assertEqual(r4.x, 151)
        self.assertEqual(r4.y, 44)

    def test_05_private_attributes(self):
        """Test for attributes being private."""
        r5 = Rectangle(11, 6, 87, 6, 91)
        d = {"_Rectangle__width": 11, "_Rectangle__height": 6,
                "_Rectangle__x": 87, "_Rectangle__y": 6, "id": 91}
        self.assertEqual(r5.__dict__, d)

    def test_06_none(self):
        """Test for None passed in."""
        with self.assertRaises(TypeError) as x:
            r6 = Rectangle(None)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'",
            str(x.exception))

    def test_07_no_args(self):
        """Test for no arguments passed in."""
        with self.assertRaises(TypeError) as x:
            r7 = Rectangle()
        self.assertEqual(
            "__init__() missing 2 required positional arguments: 'width' and 'height'",
            str(x.exception))

if __name__ == '__main__':
    unittest.main()
