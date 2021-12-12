from typing import Type
from .typed_value import TypedValue


class IntValue(TypedValue):
    def __init__(self, value: str) -> None:
        self.__value: int = int(value)

    def get_value(self) -> str:
        return str(self.__value)

    def add(self, o: TypedValue) -> TypedValue:
        other = IntValue(value=o.get_value())

        return IntValue(value=str(int(self.get_value()) + int(other.get_value())))

    def sub(self, o: TypedValue) -> TypedValue:
        other = IntValue(value=o.get_value())

        return IntValue(value=str(int(self.get_value()) - int(o.get_value())))

    def mul(self, o: TypedValue) -> TypedValue:
        other = IntValue(value=o.get_value())

        return IntValue(value=str(int(self.get_value()) * int(o.get_value())))

    def truediv(self, o: TypedValue) -> TypedValue:
        raise NotImplementedError("Cannot compute true division with int")

    def floordiv(self, o: TypedValue) -> TypedValue:
        other = IntValue(value=o.get_value())

        return IntValue(value=str(int(self.get_value()) // int(o.get_value())))
