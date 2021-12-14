from .typed_value import TypedValue
from ..utils.check_class import CheckClass


class IntValue(CheckClass, TypedValue):
    def __init__(self, value: str) -> None:
        super().__init__(value=value, check_empty_str=True)
        self.__value: int = int(value)

    def get_value(self) -> str:
        return str(self.__value)

    def add(self, o: TypedValue) -> TypedValue:
        assert o != None

        return IntValue(value=str(int(self.get_value()) + int(o.get_value())))

    def sub(self, o: TypedValue) -> TypedValue:
        assert o != None

        return IntValue(value=str(int(self.get_value()) - int(o.get_value())))

    def mul(self, o: TypedValue) -> TypedValue:
        assert o != None

        return IntValue(value=str(int(self.get_value()) * int(o.get_value())))

    def truediv(self, o: TypedValue) -> TypedValue:
        raise NotImplementedError("Cannot compute true division with int")

    def floordiv(self, o: TypedValue) -> TypedValue:
        assert o != None

        return IntValue(value=str(int(self.get_value()) // int(o.get_value())))
