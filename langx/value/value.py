from typing import Union

from .typed_value import TypedValue
from .int_value import IntValue
from .float_value import FloatValue
from .string_value import StringValue
from ..utils.check_class import CheckClass


class Value(CheckClass):
    def __init__(self, value: str, dtype: str):
        super().__init__(value=value, dtype=dtype)

        self.__value: str = value
        self.__dtype: str = dtype

    @property
    def value(self) -> str:
        return self.__value

    @property
    def dtype(self) -> str:
        return self.__dtype

    def __cast(self, value: "Value") -> TypedValue:
        if value.dtype == "int":
            return IntValue(value=value.value)
        elif value.dtype == "float":
            return FloatValue(value=value.value)
        elif value.dtype == "str":
            return StringValue(value=value.value)

        raise TypeError(f"Unsupported type: {value.dtype}")

    def __add__(self, o: "Value") -> "Value":
        assert o != None

        return Value(
            value=str(self.__cast(self).add(self.__cast(o)).get_value()),
            dtype=self.dtype,
        )

    def __sub__(self, o: "Value") -> "Value":
        assert o != None

        return Value(
            value=str(self.__cast(self).sub(self.__cast(o)).get_value()),
            dtype=self.dtype,
        )

    def __mul__(self, o: "Value") -> "Value":
        assert o != None

        return Value(
            value=str(self.__cast(self).mul(self.__cast(o)).get_value()),
            dtype=self.dtype,
        )

    def __truediv__(self, o: "Value") -> "Value":
        assert o != None

        return Value(
            value=str(self.__cast(self).truediv(self.__cast(o)).get_value()),
            dtype=self.dtype,
        )

    def __floordiv__(self, o: "Value") -> "Value":
        assert o != None

        return Value(
            value=str(self.__cast(self).floordiv(self.__cast(o)).get_value()),
            dtype=self.dtype,
        )
