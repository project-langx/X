import typing
import unittest

from langx.value.string_value import StringValue


class TestStringValue(unittest.TestCase):
    @typing.no_type_check
    def test_null_value(self) -> None:
        with self.assertRaises(AssertionError):
            StringValue(value=None)

    def test_empty_value(self) -> None:
        with self.assertRaises(AssertionError):
            StringValue(value="")

    def test_get_value(self) -> None:
        string_value: StringValue = StringValue(value="hello")
        self.assertEqual(string_value.get_value(), "hello")

    @typing.no_type_check
    def test_add_null_other(self) -> None:
        string_value: StringValue = StringValue(value="hello")
        with self.assertRaises(AssertionError):
            string_value.add(o=None)

    def test_add(self) -> None:
        string_value: StringValue = StringValue(value="hello")
        self.assertEqual(string_value.add(o=StringValue(value="world")).get_value(), "helloworld")

    def test_sub(self) -> None:
        with self.assertRaises(NotImplementedError):
            StringValue(value="hello").sub(o=StringValue(value="world"))

    def test_mul(self) -> None:
        with self.assertRaises(NotImplementedError):
            StringValue(value="hello").mul(o=StringValue(value="world"))

    def test_truediv(self) -> None:
        with self.assertRaises(NotImplementedError):
            StringValue(value="hello").truediv(o=StringValue(value="world"))

    def test_floordiv(self) -> None:
        with self.assertRaises(NotImplementedError):
            StringValue(value="hello").floordiv(o=StringValue(value="world"))