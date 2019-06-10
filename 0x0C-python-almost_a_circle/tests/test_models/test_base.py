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
        self.assertEqual(b14.__dict__, {"id": 6})

    def test_1B_private_id(self):
        """Test to make sure nb__objects is private."""
        b15 = Base(1)
        with self.assertRaises(Exception) as e:
            print(b15.nb__objects)
        self.assertEqual(
            "'Base' object has no attribute 'nb__objects'",
            str(e.exception))

    def test_1C_json_none(self):
        """Test for none in to_json_string."""
        res = Base.to_json_string(None)
        self.assertEqual(res, "[]")

    def test_1D_json_empty_list(self):
        """Test for empty in to_json_string."""
        res = Base.to_json_string([])
        self.assertEqual(res, "[]")

    def test_1E_json_str(self):
        """Test for string in to_json_string."""
        with self.assertRaises(TypeError) as e:
            res = Base.to_json_string("loki")
        self.assertEqual("list_dictionaries must be a list",
                str(e.exception))

    def test_1F_json_bool(self):
        """Test for bool in to_json_string."""
        with self.assertRaises(TypeError) as e:
            res = Base.to_json_string(True)
        self.assertEqual("list_dictionaries must be a list",
                str(e.exception))

    def test_20_json_dict(self):
        """Test for dict in to_json_string."""
        with self.assertRaises(TypeError) as e:
            res = Base.to_json_string({"a": 1})
        self.assertEqual("list_dictionaries must be a list",
                str(e.exception))

    def test_21_json_int(self):
        """Test for int in to_json_string."""
        with self.assertRaises(TypeError) as e:
            res = Base.to_json_string(1)
        self.assertEqual("list_dictionaries must be a list",
                str(e.exception))

    def test_22_json_set(self):
        """Test for set in to_json_string."""
        with self.assertRaises(TypeError) as e:
            res = Base.to_json_string({1, 2})
        self.assertEqual("list_dictionaries must be a list",
                str(e.exception))

    def test_23_json_float(self):
        """Test for float in to_json_string."""
        with self.assertRaises(TypeError) as e:
            res = Base.to_json_string(2.98)
        self.assertEqual("list_dictionaries must be a list",
                str(e.exception))

    def test_24_json_list_of_wrong_type(self):
        """Test for set in to_json_string."""
        with self.assertRaises(TypeError) as e:
            res = Base.to_json_string([1, 3, 4])
        self.assertEqual("list_dictionaries must contain dictionaries",
                str(e.exception))

    def test_25_json_list_of_mixed_types(self):
        """Test for set in to_json_string."""
        with self.assertRaises(TypeError) as e:
            res = Base.to_json_string([{"a": 1}, 5.4])
        self.assertEqual("list_dictionaries must contain dictionaries",
                str(e.exception))

    def test_26_json_list_of_multiple_dicts(self):
        """Test for set in to_json_string."""
        res = Base.to_json_string([{"a": 1}, {"b": 2}])
        self.assertEqual(type(res), str)

    def test_27_json_list_of_empty_dict(self):
        """Test for set in to_json_string."""
        res = Base.to_json_string([{}])
        self.assertEqual(res, "[{}]")

    def test_28_save_None_to_file(self):
        """Test for save_to_file method with None."""
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_29_save_empty_list_to_file(self):
        """Test for save_to_file method with empty list."""
        Base.save_to_file([])
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_2A_save_str_to_file(self):
        """Test for save_to_file method with str."""
        with self.assertRaises(TypeError) as e:
            Base.save_to_file("hello")
        self.assertEqual("list_objs must be a list",
                str(e.exception))

    def test_2B_save_dict_to_file(self):
        """Test for save_to_file method with dict."""
        with self.assertRaises(TypeError) as e:
            Base.save_to_file({"a": 1})
        self.assertEqual("list_objs must be a list",
                str(e.exception))

    def test_2C_save_int_to_file(self):
        """Test for save_to_file method with integer."""
        with self.assertRaises(TypeError) as e:
            Base.save_to_file(1)
        self.assertEqual("list_objs must be a list",
                str(e.exception))

    def test_2D_save_float_to_file(self):
        """Test for save_to_file method with float."""
        with self.assertRaises(TypeError) as e:
            Base.save_to_file(1.0)
        self.assertEqual("list_objs must be a list",
                str(e.exception))

    def test_2E_save_set_to_file(self):
        """Test for save_to_file method with set."""
        with self.assertRaises(TypeError) as e:
            Base.save_to_file({1, 2})
        self.assertEqual("list_objs must be a list",
                str(e.exception))

    def test_2F_save_bool_to_file(self):
        """Test for save_to_file method with bool."""
        with self.assertRaises(TypeError) as e:
            Base.save_to_file(True)
        self.assertEqual("list_objs must be a list",
                str(e.exception))

if __name__ == '__main__':
    unittest.main()
