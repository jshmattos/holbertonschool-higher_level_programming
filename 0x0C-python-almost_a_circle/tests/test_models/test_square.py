#!/usr/bin/python3

"""
Unittest for models/square.py
"""

import sys
import unittest
from models.square import Square

class SquareTest(unittest.TestCase):
    """Tests for square class."""

    def test_00_one_arg(self):
        """Test for one argument passed in."""
        r0 = Square(5)
        self.assertEqual(r0.id, 1)
        self.assertEqual(r0.width, 5)
        self.assertEqual(r0.height, 5)
        self.assertEqual(r0.x, 0)
        self.assertEqual(r0.y, 0)

    def test_01_two_args(self):
        """Test for two arguments passed in."""
        r1 = Square(10, 2)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 0)

    def test_02_three_args(self):
        """Test for three arguments passed in."""
        r2 = Square(98, 12, 64)
        self.assertEqual(r2.id, 3)
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
            r6 = Square(None)
        self.assertEqual(
                "width must be an integer",
                str(x.exception))

    def test_07_no_args(self):
        """Test for no arguments passed in."""
        with self.assertRaises(TypeError) as x:
            r7 = Square()
        self.assertEqual(
                "__init__() missing 1 required positional argument: 'size'",
                str(x.exception))

    def test_08_string_test(self):
        """Test for strings passed in as arguments."""
        with self.assertRaises(TypeError) as x:
            r8 = Square(10, "2")
        self.assertEqual(
                "x must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r8 = Square("10", 2)
        self.assertEqual(
                "width must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r8 = Square(10, 2, "3")
        self.assertEqual(
                "y must be an integer",
                str(x.exception))
        r8 = Square(10, 2, 0, "lol")
        self.assertEqual(r8.id, "lol")

    def test_09_float_test(self):
        """Test for floats passed in as arguments."""
        with self.assertRaises(TypeError) as x:
            r9 = Square(10, 2.1)
        self.assertEqual(
                "x must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r9 = Square(9.0, 2)
        self.assertEqual(
                "width must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r9 = Square(10, 2, 3.2131)
        self.assertEqual(
                "y must be an integer",
                str(x.exception))
        r9 = Square(10, 2, 0, 12.3)
        self.assertEqual(r9.id, 12.3)

    def test_10_list_test(self):
        """Test for lists passed in as arguments."""
        with self.assertRaises(TypeError) as x:
            r10 = Square(10, [])
        self.assertEqual(
                "x must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r10 = Square([1, 2, 3], 2)
        self.assertEqual(
                "width must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r10 = Square(10, 2, [[2, 4]])
        self.assertEqual(
                "y must be an integer",
                str(x.exception))
        r10 = Square(10, 2, 0, ["hi"])
        self.assertEqual(r10.id, ["hi"])

    def test_1A_dict_test(self):
        """Test for dicts passed in as arguments."""
        with self.assertRaises(TypeError) as x:
            r11 = Square(10, {})
        self.assertEqual(
                "x must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r11 = Square({"a":1, "b":2, "c":3}, 2)
        self.assertEqual(
                "width must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r11 = Square(10, 2, {"a":1})
        self.assertEqual(
                "y must be an integer",
                str(x.exception))
        r11 = Square(10, 2, 0, {"hi":None})
        self.assertEqual(r11.id, {"hi":None})

    def test_1B_bool_test(self):
        """Test for booleans passed in as arguments."""
        with self.assertRaises(TypeError) as x:
            r12 = Square(10, True)
        self.assertEqual(
                "x must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r12 = Square(False, 2)
        self.assertEqual(
                "width must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r12 = Square(10, 2, True)
        self.assertEqual(
                "y must be an integer",
                str(x.exception))
        r12 = Square(10, 2, 0, False)
        self.assertEqual(r12.id, False)

    def test_1C_tuple_test(self):
        """Test for tuples passed in as arguments."""
        with self.assertRaises(TypeError) as x:
            r13 = Square(10, ())
        self.assertEqual(
                "x must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r13 = Square((1, 2, 3), 2)
        self.assertEqual(
                "width must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r13 = Square(10, 2, (2, 4))
        self.assertEqual(
                "y must be an integer",
                str(x.exception))
        r13 = Square(10, 2, 0, ("hi",))
        self.assertEqual(r13.id, ("hi",))

    def test_1C_sets_test(self):
        """Test for sets passed in as arguments."""
        with self.assertRaises(TypeError) as x:
            r14 = Square(10, {})
        self.assertEqual(
                "x must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r14 = Square({1, 2, 3}, 2)
        self.assertEqual(
                "width must be an integer",
                str(x.exception))
        with self.assertRaises(TypeError) as x:
            r14 = Square(10, 2, {2, 4})
        self.assertEqual(
                "y must be an integer",
                str(x.exception))
        r14 = Square(10, 2, 0, {"hi"})
        self.assertEqual(r14.id, {"hi"})

    def test_1D_negative_ints(self):
        """Test for negative inputs."""
        with self.assertRaises(ValueError) as x:
            r15 = Square(1, -2)
        self.assertEqual(
                "x must be >= 0",
                str(x.exception))
        with self.assertRaises(ValueError) as x:
            r15 = Square(-1, -2)
        self.assertEqual(
                "width must be > 0",
                str(x.exception))
        with self.assertRaises(ValueError) as x:
            r15 = Square(1, 2, -1)
        self.assertEqual(
                "y must be >= 0",
                str(x.exception))
        r15 = Square(1, 2, 5, -1)
        self.assertEqual(r15.id, -1)

    def test_1E_zero(self):
        """Test for zero inputs."""
        r16 = Square(6, 0)
        self.assertEqual(r16.x, 0)
        with self.assertRaises(ValueError) as x:
            r16 = Square(0, 2)
        self.assertEqual(
                "width must be > 0",
                str(x.exception))
        r16 = Square(1, 0, 0, 0)
        self.assertEqual(r16.x, 0)
        self.assertEqual(r16.y, 0)
        self.assertEqual(r16.id, 0)

    def test_1F_area(self):
        """Test for area."""
        r16 = Square(3, 2)
        self.assertEqual(r16.area(), 9)
        r16 = Square(1, 20, 1)
        self.assertEqual(r16.area(), 1)
        r16 = Square(4, 5, 6, 2)
        self.assertEqual(r16.area(), 16)
        r16 = Square(9, 7, 4, 6)
        self.assertEqual(r16.area(), 81)

    def test_20_display(self):
        """Test for display."""
        r17 = Square(4, 6)
        r17 = Square(2, 4)
        pass

    def test_21_str(self):
        """Test for __str__"""
        r18 = Square(4, 6, 2, 1)
        self.assertEqual(r18.__str__(), "[Square] (1) 6/2 - 4/4")
        r18 = Square(1, 1, 0)
        self.assertEqual(r18.__str__(), "[Square] (35) 1/0 - 1/1")
        r18 = Square(1, 1)
        self.assertEqual(r18.__str__(), "[Square] (36) 1/0 - 1/1")

    def test_22_display_with_coords(self):
        """Test for display with x, y coords."""
        r19 = Square(2, 3, 2, 2)
        r19 = Square(3, 2, 1, 0)
        pass

    def test_update_args(self):
        """Test for update method."""
        r20 = Square(10, 10, 10, 10)
        r20.update(89)
        self.assertEqual(r20.__str__(), "[Square] (89) 10/10 - 10/10")
        r20.update(90, 2)
        self.assertEqual(r20.__str__(), "[Square] (90) 10/10 - 2/10")
        r20.update(91, 3, 4)
        self.assertEqual(r20.__str__(), "[Square] (91) 10/10 - 3/4")
        r20.update(92, 6, 7, 8)
        self.assertEqual(r20.__str__(), "[Square] (92) 8/10 - 6/7")
        r20 = Square(1, 1)
        r20.update(1, 2, 3, 4, 5)
        self.assertEqual(r20.__str__(), "[Square] (1) 4/5 - 2/3")

    def test_update_str(self):
        """Test for update with string."""
        r21 = Square(10, 10, 10, 1)
        with self.assertRaises(Exception) as x:
            r21.update("hello")
        self.assertEqual(
                "args must be integers",
                str(x.exception))

    def test_update_list(self):
        """Test for update with list."""
        r22 = Square(10, 10, 10, 1)
        with self.assertRaises(Exception) as x:
            r22.update([1, 2, 3])
        self.assertEqual(
                "args must be integers",
                str(x.exception))

    def test_update_tuple(self):
        """Test for update with tuple."""
        r23 = Square(10, 10, 10, 1)
        with self.assertRaises(Exception) as x:
            r23.update((1, 2, 3))
        self.assertEqual(
                "args must be integers",
                str(x.exception))

    def test_update_dict(self):
        """Test for update with dict."""
        r24 = Square(10, 10, 10, 1)
        with self.assertRaises(Exception) as x:
            r24.update({"a":1, "b":2, "c":3})
        self.assertEqual(
                "args must be integers",
                str(x.exception))

    def test_update_kwargs(self):
        """Test for update with dict."""
        r25 = Square(10, 10, 10, 1)
        r25.update(height=1)
        self.assertEqual(r25.__str__(), "[Square] (1) 10/10 - 10/1")
        r25.update(width=1, x=2)
        self.assertEqual(r25.__str__(), "[Square] (1) 2/10 - 1/1")
        r25.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r25.__str__(), "[Square] (89) 3/1 - 2/1")

    def test_args_and_kwargs(self):
        """Test for both args and kwargs."""
        r26 = Square(1, 2, 3, 4)
        r26.update(99, height=66)
        self.assertEqual(r26.__str__(), "[Square] (99) 2/3 - 1/1")

    def test_invalid_kwargs(self):
        """Test for kwargs that do not match attributes."""
        r27 = Square(1, 2, 3, 4)
        r27.update(weight=25)
        self.assertEqual(hasattr(r27, 'weight'), False)



if __name__ == '__main__':
    unittest.main()
