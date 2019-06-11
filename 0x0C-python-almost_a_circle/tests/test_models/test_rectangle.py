#!/usr/bin/python3

"""
Unittest for models/rectangle.py
"""

import sys
import os
import io
import contextlib
import unittest
from models.rectangle import Rectangle
from models.base import Base


class RectangleTest(unittest.TestCase):
    """Tests for rectangle class."""

    def setUp(self):
        Base._Base__nb_objects = 0

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
        self.assertEqual(r2.id, 1)
        self.assertEqual(r2.width, 98)
        self.assertEqual(r2.height, 12)
        self.assertEqual(r2.x, 64)
        self.assertEqual(r2.y, 0)

    def test_03_four_args(self):
        """Test for four arguments passed in."""
        r3 = Rectangle(4, 51, 96, 88)
        self.assertEqual(r3.id, 1)
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
                "__init__() missing 2 required positional arguments:" +
                " 'width' and 'height'",
                str(x.exception))

    def test_08_string_test(self):
        """Test for strings passed in as arguments."""
        with self.assertRaises(TypeError) as x:
            r8 = Rectangle(10, "2")
        self.assertEqual(
                "height must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r8 = Rectangle("10", 2)
        self.assertEqual(
                "width must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r8 = Rectangle(10, 2, "3")
        self.assertEqual(
                "x must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r8 = Rectangle(10, 2, 0, "lol")
        self.assertEqual(
                "y must be an integer",
                str(x.exception))

    def test_09_float_test(self):
        """Test for floats passed in as arguments."""
        with self.assertRaises(TypeError) as x:
            r9 = Rectangle(10, 2.1)
        self.assertEqual(
                "height must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r9 = Rectangle(9.0, 2)
        self.assertEqual(
                "width must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r9 = Rectangle(10, 2, 3.2131)
        self.assertEqual(
                "x must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r9 = Rectangle(10, 2, 0, 1662.1)
        self.assertEqual(
                "y must be an integer",
                str(x.exception))

    def test_10_list_test(self):
        """Test for lists passed in as arguments."""
        with self.assertRaises(TypeError) as x:
            r10 = Rectangle(10, [])
        self.assertEqual(
                "height must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r10 = Rectangle([1, 2, 3], 2)
        self.assertEqual(
                "width must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r10 = Rectangle(10, 2, [[2, 4]])
        self.assertEqual(
                "x must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r10 = Rectangle(10, 2, 0, ["hi"])
        self.assertEqual(
                "y must be an integer",
                str(x.exception))

    def test_1A_dict_test(self):
        """Test for dicts passed in as arguments."""
        with self.assertRaises(TypeError) as x:
            r11 = Rectangle(10, {})
        self.assertEqual(
                "height must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r11 = Rectangle({"a": 1, "b": 2, "c": 3}, 2)
        self.assertEqual(
                "width must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r11 = Rectangle(10, 2, {"a": 1})
        self.assertEqual(
                "x must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r11 = Rectangle(10, 2, 0, {"hi": None})
        self.assertEqual(
                "y must be an integer",
                str(x.exception))

    def test_1B_bool_test(self):
        """Test for booleans passed in as arguments."""
        with self.assertRaises(TypeError) as x:
            r12 = Rectangle(10, True)
        self.assertEqual(
                "height must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r12 = Rectangle(False, 2)
        self.assertEqual(
                "width must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r12 = Rectangle(10, 2, True)
        self.assertEqual(
                "x must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r12 = Rectangle(10, 2, 0, False)
        self.assertEqual(
                "y must be an integer",
                str(x.exception))

    def test_1C_tuple_test(self):
        """Test for tuples passed in as arguments."""
        with self.assertRaises(TypeError) as x:
            r13 = Rectangle(10, ())
        self.assertEqual(
                "height must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r13 = Rectangle((1, 2, 3), 2)
        self.assertEqual(
                "width must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r13 = Rectangle(10, 2, (2, 4))
        self.assertEqual(
                "x must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r13 = Rectangle(10, 2, 0, ("hi",))
        self.assertEqual(
                "y must be an integer",
                str(x.exception))

    def test_1C_sets_test(self):
        """Test for sets passed in as arguments."""
        with self.assertRaises(TypeError) as x:
            r14 = Rectangle(10, {})
        self.assertEqual(
                "height must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r14 = Rectangle({1, 2, 3}, 2)
        self.assertEqual(
                "width must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r14 = Rectangle(10, 2, {2, 4})
        self.assertEqual(
                "x must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r14 = Rectangle(10, 2, 0, {"hi"})
        self.assertEqual(
                "y must be an integer",
                str(x.exception))

    def test_1D_negative_ints(self):
        """Test for negative inputs."""
        with self.assertRaises(ValueError) as x:
            r15 = Rectangle(1, -2)
        self.assertEqual(
                "height must be > 0",
                str(x.exception))
        with self.assertRaises(ValueError) as x:
            r15 = Rectangle(-1, -2)
        self.assertEqual(
                "width must be > 0",
                str(x.exception))
        with self.assertRaises(ValueError) as x:
            r15 = Rectangle(1, 2, -1)
        self.assertEqual(
                "x must be >= 0",
                str(x.exception))
        with self.assertRaises(ValueError) as x:
            r15 = Rectangle(1, 2, 5, -1)
        self.assertEqual(
                "y must be >= 0",
                str(x.exception))

    def test_1E_zero(self):
        """Test for zero inputs."""
        with self.assertRaises(ValueError) as x:
            r16 = Rectangle(6, 0)
        self.assertEqual(
                "height must be > 0",
                str(x.exception))
        with self.assertRaises(ValueError) as x:
            r15 = Rectangle(0, 2)
        self.assertEqual(
                "width must be > 0",
                str(x.exception))
        r15 = Rectangle(1, 2, 0, 0)
        self.assertEqual(r15.x, 0)
        self.assertEqual(r15.y, 0)

    def test_1F_area(self):
        """Test for area."""
        r16 = Rectangle(3, 2)
        self.assertEqual(r16.area(), 6)
        r16 = Rectangle(1, 20, 1)
        self.assertEqual(r16.area(), 20)
        r16 = Rectangle(4, 5, 6, 2)
        self.assertEqual(r16.area(), 20)
        r16 = Rectangle(9, 7, 4, 6, 12)
        self.assertEqual(r16.area(), 63)

    def test_20_display(self):
        """Test for display."""
        r17 = Rectangle(4, 6)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r17.display()
        s = f.getvalue()
        four_by_six = "####\n####\n####\n####\n####\n####\n"
        self.assertEqual(s, four_by_six)
        r17 = Rectangle(2, 4)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r17.display()
        s = f.getvalue()
        two_by_four = "##\n##\n##\n##\n"
        self.assertEqual(s, two_by_four)

    def test_21_str(self):
        """Test for __str__"""
        r18 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r18.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        r18 = Rectangle(5, 5, 1, 1)
        self.assertEqual(r18.__str__(), "[Rectangle] (1) 1/1 - 5/5")
        r18 = Rectangle(1, 1, 0)
        self.assertEqual(r18.__str__(), "[Rectangle] (2) 0/0 - 1/1")
        r18 = Rectangle(1, 1)
        self.assertEqual(r18.__str__(), "[Rectangle] (3) 0/0 - 1/1")

    def test_22_display_with_coords(self):
        """Test for display with x, y coords."""
        r19 = Rectangle(2, 3, 2, 2)
        r19 = Rectangle(3, 2, 1, 0)
        pass

    def test_23_update_args(self):
        """Test for update method."""
        r20 = Rectangle(10, 10, 10, 10, 1)
        r20.update(89)
        self.assertEqual(r20.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r20.update(90, 2)
        self.assertEqual(r20.__str__(), "[Rectangle] (90) 10/10 - 2/10")
        r20.update(91, 3, 4)
        self.assertEqual(r20.__str__(), "[Rectangle] (91) 10/10 - 3/4")
        r20.update(92, 6, 7, 8)
        self.assertEqual(r20.__str__(), "[Rectangle] (92) 8/10 - 6/7")
        r20.update(93, 9, 10, 11, 12)
        self.assertEqual(r20.__str__(), "[Rectangle] (93) 11/12 - 9/10")
        r20 = Rectangle(1, 1)
        r20.update(1, 2, 3, 4, 5)
        self.assertEqual(r20.__str__(), "[Rectangle] (1) 4/5 - 2/3")

    def test_24_update_str(self):
        """Test for update with string."""
        r21 = Rectangle(10, 10, 10, 10, 1)
        with self.assertRaises(Exception) as x:
            r21.update("hello")
        self.assertEqual(
                "args must be integers",
                str(x.exception))

    def test_25_update_list(self):
        """Test for update with list."""
        r22 = Rectangle(10, 10, 10, 10, 1)
        with self.assertRaises(Exception) as x:
            r22.update([1, 2, 3])
        self.assertEqual(
                "args must be integers",
                str(x.exception))

    def test_26_update_tuple(self):
        """Test for update with tuple."""
        r23 = Rectangle(10, 10, 10, 10, 1)
        with self.assertRaises(Exception) as x:
            r23.update((1, 2, 3))
        self.assertEqual(
                "args must be integers",
                str(x.exception))

    def test_27_update_dict(self):
        """Test for update with dict."""
        r24 = Rectangle(10, 10, 10, 10, 1)
        with self.assertRaises(Exception) as x:
            r24.update({"a": 1, "b": 2, "c": 3})
        self.assertEqual(
                "args must be integers",
                str(x.exception))

    def test_28_update_kwargs(self):
        """Test for update with dict."""
        r25 = Rectangle(10, 10, 10, 10, 1)
        r25.update(height=1)
        self.assertEqual(r25.__str__(), "[Rectangle] (1) 10/10 - 10/1")
        r25.update(width=1, x=2)
        self.assertEqual(r25.__str__(), "[Rectangle] (1) 2/10 - 1/1")
        r25.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r25.__str__(), "[Rectangle] (89) 3/1 - 2/1")

    def test_29_args_and_kwargs(self):
        """Test for both args and kwargs."""
        r26 = Rectangle(1, 2, 3, 4, 5)
        r26.update(99, height=66)
        self.assertEqual(r26.__str__(), "[Rectangle] (99) 3/4 - 1/2")

    def test_30_invalid_kwargs(self):
        """Test for kwargs that do not match attributes."""
        r27 = Rectangle(1, 2, 3, 4, 5)
        r27.update(weight=25)
        self.assertEqual(hasattr(r27, 'weight'), False)

    def test_31_to_dictionary(self):
        """Test for dictionary representation of rectangle."""
        r28 = Rectangle(10, 2, 1, 9)
        r28_d = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r28.to_dictionary(), r28_d)
        self.assertEqual(r28.to_dictionary() is r28_d, False)
        r28 = Rectangle(9, 4, 15)
        r28_d = {'width': 9, 'height': 4, 'x': 15, 'id': 2, 'y': 0}
        self.assertEqual(r28.to_dictionary(), r28_d)
        self.assertEqual(r28.to_dictionary() is r28_d, False)
        r28 = Rectangle(62, 414)
        r28_d = {'width': 62, 'height': 414, 'x': 0, 'id': 3, 'y': 0}
        self.assertEqual(r28.to_dictionary(), r28_d)
        self.assertEqual(r28.to_dictionary() is r28_d, False)
        r28 = Rectangle(1, 2, 3, 4, 5)
        r28_d = {'width': 1, 'height': 2, 'x': 3, 'id': 5, 'y': 4}
        self.assertEqual(r28.to_dictionary(), r28_d)
        self.assertEqual(r28.to_dictionary() is r28_d, False)

    def test_32_to_json_string(self):
        """Test for json string of rectangle."""
        r29 = Rectangle(10, 7, 2, 8)
        d = r29.to_dictionary()
        json_d = Base.to_json_string([d])
        self.assertEqual(type(json_d), str)
        self.assertEqual(d, {'height': 7, 'id': 1, 'width': 10, 'x': 2, 'y': 8})

    def test_33_save_to_file(self):
        """Test for save_to_file method."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        res = '[{"x": 2, "y": 8, "id": 2, "height": 7, "width": 10},' + \
            ' {"x": 0, "y": 0, "id": 3, "height": 4, "width": 2}]'
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), len(res))

    def test_34_from_json_string(self):
        """Test for from_json_string method."""
        list_input = [{'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        l = [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}]
        self.assertEqual(list_output, l)

    def test_35_create(self):
        """Test for create method with rectangle."""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual((r1 == r2), False)
        self.assertEqual((r1 is r2), False)

    def test_36_create_none(self):
        """Test for create method with None."""
        b1 = Rectangle(1, 1)
        b1_dictionary = b1.to_dictionary()
        with self.assertRaises(TypeError) as e:
            b2 = Rectangle.create(None)
        self.assertEqual("create() takes 1 positional argument but 2 were given",
            str(e.exception))

    def test_37_create_string(self):
        """Test for create method with string."""
        b1 = Rectangle(1, 1)
        b1_dictionary = b1.to_dictionary()
        with self.assertRaises(TypeError) as e:
            b2 = Rectangle.create("hello")
        self.assertEqual("create() takes 1 positional argument but 2 were given",
            str(e.exception))

    def test_38_create_list(self):
        """Test for create method with list."""
        b1 = Rectangle(1, 1)
        b1_dictionary = b1.to_dictionary()
        with self.assertRaises(TypeError) as e:
            b2 = Rectangle.create([1, 2, 3])
        self.assertEqual("create() takes 1 positional argument but 2 were given",
            str(e.exception))

    def test_39_create_int(self):
        """Test for create method with int."""
        b1 = Rectangle(1, 1)
        b1_dictionary = b1.to_dictionary()
        with self.assertRaises(TypeError) as e:
            b2 = Rectangle.create(1)
        self.assertEqual("create() takes 1 positional argument but 2 were given",
            str(e.exception))

    def test_40_create_float(self):
        """Test for create method with float."""
        b1 = Rectangle(1, 1)
        b1_dictionary = b1.to_dictionary()
        with self.assertRaises(TypeError) as e:
            b2 = Rectangle.create(1.0)
        self.assertEqual("create() takes 1 positional argument but 2 were given",
            str(e.exception))

    def test_41_create_set(self):
        """Test for create method with set."""
        b1 = Rectangle(1, 1)
        b1_dictionary = b1.to_dictionary()
        with self.assertRaises(TypeError) as e:
            b2 = Rectangle.create({1, 2, 3})
        self.assertEqual("create() takes 1 positional argument but 2 were given",
            str(e.exception))

    def test_42_create_invalid_key(self):
        """Test for create method with set."""
        b1 = Rectangle(1, 2, 3, 4, 5)
        b1_dictionary = b1.to_dictionary()
        b2 = Rectangle.create(volume=1)
        self.assertEqual(b1.__dict__ == b2.__dict__, False)

    def test_43_create_empty(self):
        """Test for create method with set."""
        with self.assertRaises(ValueError) as e:
            b = Rectangle.create()
        self.assertEqual("dictionary cannot be empty",
                str(e.exception))

    def test_44_load_from_files(self):
        """Test for load_from_files."""
        os.remove("Rectangle.json")
        rect_list = Rectangle.load_from_file()
        self.assertEqual(rect_list, [])

    def test_45_save_to_csv(self):
        """Test for save_to_csv."""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9)
        r3 = Rectangle(10, 11, 12)
        r4 = Rectangle(13, 14)
        list_rectangles_input = [r1, r2, r3, r4]
        Rectangle.save_to_file_csv(list_rectangles_input)
        with open("Rectangle.csv", "r") as f:
            data = f.readlines()
        self.assertEqual(data[0], 'id,width,height,x,y\n')
        self.assertEqual(data[1], '5,1,2,3,4\n')
        self.assertEqual(data[2], '1,6,7,8,9\n')
        self.assertEqual(data[3], '2,10,11,12,0\n')
        self.assertEqual(data[4], '3,13,14,0,0\n')

if __name__ == '__main__':
    unittest.main()
