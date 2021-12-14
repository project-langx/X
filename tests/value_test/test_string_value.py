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