#!/usr/bin/python3

"""
Unittest for models/square.py
"""

import sys
import os
import unittest
import io
import contextlib
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class SquareTest(unittest.TestCase):
    """Tests for square class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_00_one_arg(self):
        """Test for one argument passed in."""
        s = Square(5)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_01_two_args(self):
        """Test for two arguments passed in."""
        r1 = Square(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 0)

    def test_02_three_args(self):
        """Test for three arguments passed in."""
        r2 = Square(98, 12, 64)
        self.assertEqual(r2.id, 1)
        self.assertEqual(r2.width, 98)
        self.assertEqual(r2.height, 98)
        self.assertEqual(r2.x, 12)
        self.assertEqual(r2.y, 64)

    def test_03_four_args(self):
        """Test for four arguments passed in."""
        r3 = Square(4, 51, 96, 88)
        self.assertEqual(r3.id, 88)
        self.assertEqual(r3.width, 4)
        self.assertEqual(r3.height, 4)
        self.assertEqual(r3.x, 51)
        self.assertEqual(r3.y, 96)

    def test_04_five_args(self):
        """Test for five arguments passed in."""
        pass

    def test_05_private_attributes(self):
        """Test for attributes being private."""
        r5 = Square(11, 6, 87, 6)
        d = {"_Rectangle__width": 11, "_Rectangle__height": 11,
             "_Rectangle__x": 6, "_Rectangle__y": 87, "id": 6}
        self.assertEqual(r5.__dict__, d)

    def test_06_none(self):
        """Test for None passed in."""
        with self.assertRaises(TypeError) as x:
            r = Square(None)
        self.assertEqual(
            "width must be an integer",
            str(x.exception))

    def test_07_no_args(self):
        """Test for no arguments passed in."""
        with self.assertRaises(TypeError) as x:
            r = Square()
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'size'",
            str(x.exception))

    def test_08_string_test(self):
        """Test for strings passed in as arguments."""
        with self.assertRaises(TypeError) as x:
            r = Square(10, "2")
        self.assertEqual(
            "x must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square("10", 2)
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square(10, 2, "3")
        self.assertEqual(
            "y must be an integer",
            str(x.exception))
        r = Square(10, 2, 0, "lol")
        self.assertEqual(r.id, "lol")

    def test_09_float_test(self):
        """Test for floats passed in as arguments."""
        with self.assertRaises(TypeError) as x:
            r = Square(10, 2.1)
        self.assertEqual(
            "x must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square(9.0, 2)
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square(10, 2, 3.2131)
        self.assertEqual(
            "y must be an integer",
            str(x.exception))
        r = Square(10, 2, 0, 12.3)
        self.assertEqual(r.id, 12.3)

    def test_10_list_test(self):
        """Test for lists passed in as arguments."""
        with self.assertRaises(TypeError) as x:
            r = Square(10, [])
        self.assertEqual(
            "x must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square([1, 2, 3], 2)
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square(10, 2, [[2, 4]])
        self.assertEqual(
            "y must be an integer",
            str(x.exception))
        r = Square(10, 2, 0, ["hi"])
        self.assertEqual(r.id, ["hi"])

    def test_1A_dict_test(self):
        """Test for dicts passed in as arguments."""
        with self.assertRaises(TypeError) as x:
            r = Square(10, {})
        self.assertEqual(
            "x must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square({"a": 1, "b": 2, "c": 3}, 2)
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square(10, 2, {"a": 1})
        self.assertEqual(
            "y must be an integer",
            str(x.exception))
        r = Square(10, 2, 0, {"hi": None})
        self.assertEqual(r.id, {"hi": None})

    def test_1B_bool_test(self):
        """Test for booleans passed in as arguments."""
        with self.assertRaises(TypeError) as x:
            r = Square(10, True)
        self.assertEqual(
            "x must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square(False, 2)
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square(10, 2, True)
        self.assertEqual(
            "y must be an integer",
            str(x.exception))
        r = Square(10, 2, 0, False)
        self.assertEqual(r.id, False)

    def test_1C_tuple_test(self):
        """Test for tuples passed in as arguments."""
        with self.assertRaises(TypeError) as x:
            r = Square(10, ())
        self.assertEqual(
            "x must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square((1, 2, 3), 2)
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square(10, 2, (2, 4))
        self.assertEqual(
            "y must be an integer",
            str(x.exception))
        r = Square(10, 2, 0, ("hi",))
        self.assertEqual(r.id, ("hi",))

    def test_1C_sets_test(self):
        """Test for sets passed in as arguments."""
        with self.assertRaises(TypeError) as x:
            r = Square(10, {})
        self.assertEqual(
            "x must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square({1, 2, 3}, 2)
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square(10, 2, {2, 4})
        self.assertEqual(
            "y must be an integer",
            str(x.exception))
        r = Square(10, 2, 0, {"hi"})
        self.assertEqual(r.id, {"hi"})

    def test_1D_negative_ints(self):
        """Test for negative inputs."""
        with self.assertRaises(ValueError) as x:
            r = Square(1, -2)
        self.assertEqual(
            "x must be >= 0",
            str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Square(-1, -2)
        self.assertEqual(
            "width must be > 0",
            str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Square(1, 2, -1)
        self.assertEqual(
            "y must be >= 0",
            str(x.exception))
        r = Square(1, 2, 5, -1)
        self.assertEqual(r.id, -1)

    def test_1E_zero(self):
        """Test for zero inputs."""
        r = Square(6, 0)
        self.assertEqual(r.x, 0)
        with self.assertRaises(ValueError) as x:
            r = Square(0, 2)
        self.assertEqual(
            "width must be > 0",
            str(x.exception))
        r = Square(1, 0, 0, 0)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 0)

    def test_1F_area(self):
        """Test for area."""
        r = Square(3, 2)
        self.assertEqual(r.area(), 9)
        r = Square(1, 20, 1)
        self.assertEqual(r.area(), 1)
        r = Square(4, 5, 6, 2)
        self.assertEqual(r.area(), 16)
        r = Square(9, 7, 4, 6)
        self.assertEqual(r.area(), 81)

    def test_20_display(self):
        """Test for display."""
        s = Square(2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            s.display()
        s = f.getvalue()
        output = "##\n##\n"
        self.assertEqual(s, output)
        s = Square(2, 4)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            s.display()
        s = f.getvalue()
        output = "    ##\n    ##\n"
        self.assertEqual(s, output)

    def test_21_str(self):
        """Test for __str__"""
        r = Square(4, 6, 2, 1)
        self.assertEqual(r.__str__(), "[Square] (1) 6/2 - 4")
        r = Square(1, 1, 0)
        self.assertEqual(r.__str__(), "[Square] (1) 1/0 - 1")
        r = Square(1, 1)
        self.assertEqual(r.__str__(), "[Square] (2) 1/0 - 1")

    def test_22_display_with_coords(self):
        """Test for display with x, y coords."""
        s = Square(2, 3, 2, 2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            s.display()
        s = f.getvalue()
        output = "\n\n   ##\n   ##\n"
        self.assertEqual(s, output)
        s = Square(1, 0, 1)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            s.display()
        s = f.getvalue()
        output = "\n#\n"
        self.assertEqual(s, output)
        s = Square(2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            s.display()
        s = f.getvalue()
        output = "##\n##\n"
        self.assertEqual(s, output)

    def test_23_update_args(self):
        """Test for update method."""
        r = Square(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.__str__(), "[Square] (89) 10/10 - 10")
        r.update(90, 2)
        self.assertEqual(r.__str__(), "[Square] (90) 10/10 - 2")
        r.update(91, 3, 4)
        self.assertEqual(r.__str__(), "[Square] (91) 4/10 - 3")
        r.update(92, 6, 7, 8)
        self.assertEqual(r.__str__(), "[Square] (92) 7/8 - 6")
        r = Square(1, 1)
        r.update(7, 2, 3, 4)
        self.assertEqual(r.__str__(), "[Square] (7) 3/4 - 2")

    def test_28_update_kwargs(self):
        """Test for update with dict."""
        r = Square(10, 10, 10, 1)
        r.update(height=1)
        self.assertEqual(r.__str__(), "[Square] (1) 10/10 - 10")
        r.update(width=1, x=2)
        self.assertEqual(r.__str__(), "[Square] (1) 2/10 - 1")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r.__str__(), "[Square] (89) 3/1 - 2")

    def test_29_args_and_kwargs(self):
        """Test for both args and kwargs."""
        r = Square(1, 2, 3, 4)
        r.update(99, height=66)
        self.assertEqual(r.__str__(), "[Square] (99) 2/3 - 1")

    def test_30_invalid_kwargs(self):
        """Test for kwargs that do not match attributes."""
        r = Square(1, 2, 3, 4)
        r.update(weight=25)
        self.assertEqual(hasattr(r, 'weight'), False)

    def test_3A_size(self):
        """Test for size attr."""
        r = Square(5)
        self.assertEqual(r.size, 5)
        r.size = 25
        self.assertEqual(r.size, 25)
        with self.assertRaises(TypeError) as x:
            r.size = "hello"
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r.size = [1, 2]
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r.size = (2,)
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r.size = {"a": 1}
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r.size = True
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r.size = {1, 2}
        self.assertEqual(
            "width must be an integer",
            str(x.exception))

    def test_3B_to_dictionary(self):
        """Returns the dictionary representation of rectangle."""
        r = Square(10, 2, 1, 9)
        r_d = {'x': 2, 'y': 1, 'id': 9}
        self.assertEqual(r.to_dictionary(), r_d)
        self.assertEqual(r.to_dictionary() is r_d, False)
        r = Square(9, 4, 15)
        r_d = {'x': 4, 'id': 1, 'y': 15}
        self.assertEqual(r.to_dictionary(), r_d)
        self.assertEqual(r.to_dictionary() is r_d, False)
        r = Square(62, 414)
        r_d = {'x': 414, 'id': 2, 'y': 0}
        self.assertEqual(r.to_dictionary(), r_d)
        self.assertEqual(r.to_dictionary() is r_d, False)

    def test_3C_to_json_string(self):
        """Test for json string of rectangle."""
        r = Square(10, 7, 2)
        d = r.to_dictionary()
        json_d = Base.to_json_string([d])
        self.assertEqual(type(json_d), str)
        self.assertEqual(d, {'id': 1, 'x': 7, 'y': 2})

    def test_3D_save_to_file(self):
        """Test for save_to_file method."""
        r1 = Square(10, 7, 2)
        r2 = Square(2, 4)
        Square.save_to_file([r1, r2])
        res = '[{"x": 7, "y": 2, "id": 1},' + \
            ' {"x": 4, "y": 0, "id": 2}]'
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), len(res))

    def test_3E_save_to_file_different_types(self):
        """Test for save_to_file method with different types."""
        r = Rectangle(1, 2)
        s = Square(3, 4)
        with self.assertRaises(ValueError) as e:
            Base.save_to_file([r, s])
        self.assertEqual("all elements of list_objs must match",
                         str(e.exception))
        with self.assertRaises(ValueError) as e:
            Base.save_to_file([s, r])
        self.assertEqual("all elements of list_objs must match",
                         str(e.exception))

    def test_3F_from_json_string(self):
        """Test for from_json_string method."""
        list_input = [{'id': 89, 'size': 10},
                      {'id': 7, 'size': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        l = [{'size': 10, 'id': 89}, {'size': 7, 'id': 7}]
        self.assertEqual(list_output, l)

    def test_40_create(self):
        """Test for create method with square."""
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual((s1 == s2), False)
        self.assertEqual((s1 is s2), False)

    def test_41_load_from_files(self):
        """Test for load_from_files."""
        os.remove("Square.json")
        square_list = Square.load_from_file()
        self.assertEqual(square_list, [])
"""
    def test_42_save_to_csv(self):
        Test for save_to_csv.
        r1 = Square(1, 2, 3, 4)
        r2 = Square(5, 6, 7)
        r3 = Square(8, 9)
        r4 = Square(10)
        list_rectangles_input = [r1, r2, r3, r4]
        Square.save_to_file_csv(list_rectangles_input)
        with open("Square.csv", "r") as f:
            data = f.readlines()
        self.assertEqual(data[0], 'id,size,x,y\n')
        self.assertEqual(data[1], '4,1,2,3\n')
        self.assertEqual(data[2], '1,5,6,7\n')
        self.assertEqual(data[3], '2,8,9,0\n')
        self.assertEqual(data[4], '3,10,0,0\n')
"""

if __name__ == '__main__':
    unittest.main()
