from .typed_value import TypedValue
from ..utils.check_class import CheckClass


class FloatValue(CheckClass, TypedValue):
    def __init__(self, value: str) -> None:
        super().__init__(value=value, check_empty_str=True)
        self.__value: float = float(value)

    def get_value(self) -> str:
        return str(self.__value)

    def add(self, o: TypedValue) -> TypedValue:
        assert o != None

        return FloatValue(value=str(float(self.get_value()) + float(o.get_value())))

    def sub(self, o: TypedValue) -> TypedValue:
        assert o != None

        return FloatValue(value=str(float(self.get_value()) - float(o.get_value())))

    def mul(self, o: TypedValue) -> TypedValue:
        assert o != None

        return FloatValue(value=str(float(self.get_value()) * float(o.get_value())))

    def truediv(self, o: TypedValue) -> TypedValue:
        assert o != None

        return FloatValue(value=str(float(self.get_value()) / float(o.get_value())))

    def floordiv(self, o: TypedValue) -> TypedValue:
        raise NotImplementedError("Cannot compute floor division with float")
