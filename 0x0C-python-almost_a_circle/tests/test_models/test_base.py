#!/usr/bin/python3

"""
Unittest for models/base.py
"""

import unittest
from models.base import Base

class BaseTest(unittest.TestCase):
    """Tests for base class."""

    def test_00_correct_id(self):
        """Test for correct id attribute."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_01_custom_id(self):
        """Test for custom id."""
        b4 = Base(98)
        self.assertEqual(b4.id, 98)

    def test_02_correct_id_after_custom(self):
        """Test for no id after a custom entry."""
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_03_string_input(self):
        """Test for string input."""
        b6 = Base("hello")
        self.assertEqual(b6.id, "hello")

    def test_04_none_input(self):
        """Test for None input."""
        b7 = Base(None)
        self.assertEqual(b7.id, 5)

    def test_05_zero_input(self):
        """Test for zero input."""
        b8 = Base(0)
        self.assertEqual(b8.id, 0)

    def test_06_negative_input(self):
        """Test for negative input."""
        b9 = Base(-5)
        self.assertEqual(b9.id, -5)

    def test_07_list_input(self):
        """Test for list input."""
        b10 = Base([1, 2, 3])
        self.assertEqual(b10.id, [1, 2, 3])

    def test_08_dict_input(self):
        """Test for dict input."""
        b11 = Base({"hello": "world"})
        self.assertEqual(b11.id, {"hello": "world"})

    def test_09_float_input(self):
        """Test for float input."""
        b12 = Base(9.1)
        self.assertEqual(b12.id, 9.1)

    def test_10_tuple_input(self):
        """Test for tuple input."""
        b13 = Base((1,))
        self.assertEqual(b13.id, (1,))

    def test_1A_class_type(self):
        """Test for correct class type."""
        b14 = Base()
        self.assertEqual(str(type(b14)), "<class 'models.base.Base'>")
        self.assertEqual(b14.__dict__, {"id":6})

    def test_1B_private_id(self):
        """Test to make sure nb__objects is private."""
        b15 = Base(1)
        with self.assertRaises(Exception) as e:
            print(b15.nb__objects)
        self.assertEqual(
            "'Base' object has no attribute 'nb__objects'",
            str(e.exception))

if __name__ == '__main__':
    unittest.main()
