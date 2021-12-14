import typing
import unittest

from langx.value.int_value import IntValue
from langx.value.typed_value import TypedValue


class TestIntValue(unittest.TestCase):
    @typing.no_type_check
    def test_null_value(self) -> None:
        with self.assertRaises(AssertionError):
            IntValue(value=None)

    def test_empty_value(self) -> None:
        with self.assertRaises(AssertionError):
            IntValue(value="")

    def test_get_value(self) -> None:
        int_value: TypedValue = IntValue(value="123")
        self.assertEqual(int_value.get_value(), "123")

    @typing.no_type_check
    def test_add_null_other(self) -> None:
        int_value: TypedValue = IntValue(value="123")
        with self.assertRaises(AssertionError):
            int_value.add(o=None)

    def test_add(self) -> None:
        int_value: TypedValue = IntValue(value="123")
        self.assertEqual(int_value.add(o=IntValue(value="456")).get_value(), "579")

    @typing.no_type_check
    def test_sub_null_other(self) -> None:
        int_value: TypedValue = IntValue(value="123")
        with self.assertRaises(AssertionError):
            int_value.sub(o=None)

    def test_sub(self) -> None:
        int_value: TypedValue = IntValue(value="123")
        self.assertEqual(int_value.sub(o=IntValue(value="456")).get_value(), "-333")

    @typing.no_type_check
    def test_mul_null_other(self) -> None:
        int_value: TypedValue = IntValue(value="123")
        with self.assertRaises(AssertionError):
            int_value.mul(o=None)

    def test_mul(self) -> None:
        int_value: TypedValue = IntValue(value="123")
        self.assertEqual(int_value.mul(o=IntValue(value="456")).get_value(), "56088")

    def test_truediv(self) -> None:
        with self.assertRaises(NotImplementedError):
            IntValue(value="123").truediv(o=IntValue(value="456"))

    @typing.no_type_check
    def test_floordiv_null_other(self) -> None:
        int_value: TypedValue = IntValue(value="123")
        with self.assertRaises(AssertionError):
            int_value.floordiv(o=None)

    def test_floordiv(self) -> None:
        int_value: TypedValue = IntValue(value="5")
        self.assertEqual(int_value.floordiv(o=IntValue(value="2")).get_value(), "2")
