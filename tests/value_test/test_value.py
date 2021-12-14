import typing
import unittest

from langx.value.value import Value


class TestValue(unittest.TestCase):
    @typing.no_type_check
    def test_null_value(self) -> None:
        with self.assertRaises(AssertionError):
            Value(value=None, dtype="str")

    @typing.no_type_check
    def test_null_dtype(self) -> None:
        with self.assertRaises(AssertionError):
            Value(value="hello", dtype=None)

    def test_value_property(self) -> None:
        value: Value = Value(value="hello", dtype="str")
        self.assertEqual(value.value, "hello")

        value = Value(value="123", dtype="int")
        self.assertEqual(value.value, "123")

        value = Value(value="123.456", dtype="float")
        self.assertEqual(value.value, "123.456")

    def test_dtype_property(self) -> None:
        value: Value = Value(value="hello", dtype="str")
        self.assertEqual(value.dtype, "str")

        value = Value(value="123", dtype="int")
        self.assertEqual(value.dtype, "int")

        value = Value(value="123.456", dtype="float")
        self.assertEqual(value.dtype, "float")

    @typing.no_type_check
    def test_add_null_other(self) -> None:
        value: Value = Value(value="hello", dtype="str")
        with self.assertRaises(AssertionError):
            value + None

        value = Value(value="123", dtype="int")
        with self.assertRaises(AssertionError):
            value + None

        value = Value(value="123.456", dtype="float")
        with self.assertRaises(AssertionError):
            value + None

    def test_add(self) -> None:
        value: Value = Value(value="hello", dtype="str")
        other: Value = Value(value="world", dtype="str")
        self.assertEqual((value + other).value, "helloworld")

        value = Value(value="123", dtype="int")
        other = Value(value="456", dtype="int")
        self.assertEqual((value + other).value, "579")

        value = Value(value="123.456", dtype="float")
        other = Value(value="789.123", dtype="float")
        self.assertEqual((value + other).value, "912.5790000000001")

    @typing.no_type_check
    def test_sub_null_other(self) -> None:
        value: Value = Value(value="hello", dtype="str")
        with self.assertRaises(AssertionError):
            value - None

        value = Value(value="123", dtype="int")
        with self.assertRaises(AssertionError):
            value - None

        value = Value(value="123.456", dtype="float")
        with self.assertRaises(AssertionError):
            value - None

    def test_sub(self) -> None:
        value: Value = Value(value="hello", dtype="str")
        other: Value = Value(value="world", dtype="str")
        with self.assertRaises(NotImplementedError):
            value - other

        value = Value(value="123", dtype="int")
        other = Value(value="456", dtype="int")
        self.assertEqual((value - other).value, "-333")

        value = Value(value="123.456", dtype="float")
        other = Value(value="789.123", dtype="float")
        self.assertEqual((value - other).value, "-665.667")

    @typing.no_type_check
    def test_mul_null_other(self) -> None:
        value: Value = Value(value="hello", dtype="str")
        with self.assertRaises(AssertionError):
            value * None

        value = Value(value="123", dtype="int")
        with self.assertRaises(AssertionError):
            value * None

        value = Value(value="123.456", dtype="float")
        with self.assertRaises(AssertionError):
            value * None

    def test_mul(self) -> None:
        value: Value = Value(value="hello", dtype="str")
        other: Value = Value(value="world", dtype="str")
        with self.assertRaises(NotImplementedError):
            value * other

        value = Value(value="123", dtype="int")
        other = Value(value="456", dtype="int")
        self.assertEqual((value * other).value, "56088")

        value = Value(value="123.456", dtype="float")
        other = Value(value="789.123", dtype="float")
        self.assertEqual((value * other).value, "97421.96908800001")

    @typing.no_type_check
    def test_truediv_null_other(self) -> None:
        value: Value = Value(value="hello", dtype="str")
        with self.assertRaises(AssertionError):
            value / None

        value = Value(value="123", dtype="int")
        with self.assertRaises(AssertionError):
            value / None

        value = Value(value="123.456", dtype="float")
        with self.assertRaises(AssertionError):
            value / None

    def test_truediv(self) -> None:
        value: Value = Value(value="hello", dtype="str")
        other: Value = Value(value="world", dtype="str")
        with self.assertRaises(NotImplementedError):
            value / other

        value = Value(value="123", dtype="int")
        other = Value(value="456", dtype="int")
        with self.assertRaises(NotImplementedError):
            value / other

        value = Value(value="5", dtype="float")
        other = Value(value="2", dtype="float")
        self.assertEqual((value / other).value, "2.5")

    @typing.no_type_check
    def test_floordiv_null_other(self) -> None:
        value: Value = Value(value="hello", dtype="str")
        with self.assertRaises(AssertionError):
            value // None

        value = Value(value="123", dtype="int")
        with self.assertRaises(AssertionError):
            value // None

        value = Value(value="123.456", dtype="float")
        with self.assertRaises(AssertionError):
            value // None

    def test_floordiv(self) -> None:
        value: Value = Value(value="hello", dtype="str")
        other: Value = Value(value="world", dtype="str")
        with self.assertRaises(NotImplementedError):
            value // other

        value = Value(value="5", dtype="int")
        other = Value(value="2", dtype="int")
        self.assertEqual((value // other).value, "2")

        value = Value(value="5", dtype="float")
        other = Value(value="2", dtype="float")
        with self.assertRaises(NotImplementedError):
            value // other
