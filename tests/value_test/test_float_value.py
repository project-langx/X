import typing
import unittest

from langx.value.float_value import FloatValue


class TestFloatValue(unittest.TestCase):
    @typing.no_type_check
    def test_null_value(self) -> None:
        with self.assertRaises(AssertionError):
            FloatValue(value=None)

    def test_empty_value(self) -> None:
        with self.assertRaises(AssertionError):
            FloatValue(value="")

    def test_get_value(self) -> None:
        float_value: FloatValue = FloatValue(value="123.456")
        self.assertEqual(float_value.get_value(), "123.456")

    @typing.no_type_check
    def test_add_null_other(self) -> None:
        float_value: FloatValue = FloatValue(value="123.456")
        with self.assertRaises(AssertionError):
            float_value.add(o=None)

    def test_add(self) -> None:
        float_value: FloatValue = FloatValue(value="123.456")
        self.assertEqual(float_value.add(o=FloatValue(value="456.789")).get_value(), "580.245")

    @typing.no_type_check
    def test_sub_null_other(self) -> None:
        float_value: FloatValue = FloatValue(value="123.456")
        with self.assertRaises(AssertionError):
            float_value.sub(o=None)

    def test_sub(self) -> None:
        float_value: FloatValue = FloatValue(value="123.456")
        self.assertEqual(float_value.sub(o=FloatValue(value="456.789")).get_value(), "-333.33299999999997")

    @typing.no_type_check
    def test_mul_null_other(self) -> None:
        float_value: FloatValue = FloatValue(value="123.456")
        with self.assertRaises(AssertionError):
            float_value.mul(o=None)

    def test_mul(self) -> None:
        float_value: FloatValue = FloatValue(value="123.456")
        self.assertEqual(float_value.mul(o=FloatValue(value="456.789")).get_value(), "56393.342784")

    @typing.no_type_check
    def test_truediv_null_other(self) -> None:
        with self.assertRaises(AssertionError):
            FloatValue(value="123.456").truediv(o=None)

    def test_truediv(self) -> None:
        float_value: FloatValue = FloatValue(value="5")
        self.assertEqual(float_value.truediv(o=FloatValue(value="2")).get_value(), "2.5")

    def test_floordiv(self) -> None:
        with self.assertRaises(NotImplementedError):
            FloatValue(value="123.456").floordiv(o=FloatValue(value="456.789"))