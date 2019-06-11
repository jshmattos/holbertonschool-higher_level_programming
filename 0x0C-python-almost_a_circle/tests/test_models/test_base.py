#!/usr/bin/python3

"""
Unittest for models/base.py
"""

import unittest
import os
from models.base import Base


class BaseTest(unittest.TestCase):
    """Tests for base class."""

    def setUp(self):
        Base._Base__nb_objects = 0

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
        b = Base(98)
        self.assertEqual(b.id, 98)

    def test_02_correct_id_after_custom(self):
        """Test for no id after a custom entry."""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_03_string_input(self):
        """Test for string input."""
        b = Base("hello")
        self.assertEqual(b.id, "hello")

    def test_04_none_input(self):
        """Test for None input."""
        b = Base(None)
        self.assertEqual(b.id, 1)

    def test_05_zero_input(self):
        """Test for zero input."""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_06_negative_input(self):
        """Test for negative input."""
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_07_list_input(self):
        """Test for list input."""
        b = Base([1, 2, 3])
        self.assertEqual(b.id, [1, 2, 3])

    def test_08_dict_input(self):
        """Test for dict input."""
        b = Base({"hello": "world"})
        self.assertEqual(b.id, {"hello": "world"})

    def test_09_float_input(self):
        """Test for float input."""
        b = Base(9.1)
        self.assertEqual(b.id, 9.1)

    def test_10_tuple_input(self):
        """Test for tuple input."""
        b = Base((1,))
        self.assertEqual(b.id, (1,))

    def test_1A_class_type(self):
        """Test for correct class type."""
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})

    def test_1B_private_id(self):
        """Test to make sure nb__objects is private."""
        b = Base(1)
        with self.assertRaises(Exception) as e:
            print(b.nb__objects)
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

    def test_30_from_json_string_None(self):
        """Test for from_json_method with None."""
        list_output = Base.from_json_string(None)
        self.assertEqual(list_output, [])

    def test_31_from_json_string_empty_string(self):
        """Test for from_json_method with empty string."""
        list_output = Base.from_json_string("")
        self.assertEqual(list_output, [])

    def test_31a_from_json_string_no_arg(self):
        """Test for from_json_method with empty string."""
        with self.assertRaises(TypeError) as e:
            list_output = Base.from_json_string()
        self.assertEqual("from_json_string() missing 1 required positional " +
                         "argument: 'json_string'",
                         str(e.exception))

    def test_32_from_json_string_list(self):
        """Test for from_json_method with list."""
        with self.assertRaises(TypeError) as e:
            Base.from_json_string([1, 2, 3])
        self.assertEqual("json_string must be a string",
                         str(e.exception))

    def test_33_from_json_string_dict(self):
        """Test for from_json_method with dict."""
        with self.assertRaises(TypeError) as e:
            Base.from_json_string({"a": 1})
        self.assertEqual("json_string must be a string",
                         str(e.exception))

    def test_34_from_json_string_int(self):
        """Test for from_json_method with int."""
        with self.assertRaises(TypeError) as e:
            Base.from_json_string(1)
        self.assertEqual("json_string must be a string",
                         str(e.exception))

    def test_35_from_json_string_bool(self):
        """Test for from_json_method with bool."""
        with self.assertRaises(TypeError) as e:
            Base.from_json_string(False)
        self.assertEqual("json_string must be a string",
                         str(e.exception))

    def test_36_from_json_string_float(self):
        """Test for from_json_method with float."""
        with self.assertRaises(TypeError) as e:
            Base.from_json_string(8.7)
        self.assertEqual("json_string must be a string",
                         str(e.exception))

    def test_37_from_json_string_set(self):
        """Test for from_json_method with set."""
        with self.assertRaises(TypeError) as e:
            Base.from_json_string({1, 2})
        self.assertEqual("json_string must be a string",
                         str(e.exception))

    def test_38_from_json_string_non_dicts(self):
        """Test for from_json_method with empty_dicts."""
        list_input = [{}, {}]
        json_list_input = Base.to_json_string(list_input)
        list_output = Base.from_json_string(json_list_input)
        self.assertEqual(list_output, [{}, {}])

    def test_39_load_from_files(self):
        """Test for load_from_files."""
        os.remove("Base.json")
        base_list = Base.load_from_file()
        self.assertEqual(base_list, [])


if __name__ == '__main__':
    unittest.main()
