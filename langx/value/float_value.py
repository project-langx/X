from .typed_value import TypedValue


class FloatValue(TypedValue):
    def __init__(self, value: str) -> None:
        self.__value: float = float(value)

    def get_value(self) -> str:
        return str(self.__value)

    def add(self, o: TypedValue) -> TypedValue:
        other = FloatValue(value=str(o.get_value()))

        return FloatValue(value=str(float(self.get_value()) + float(other.get_value())))

    def sub(self, o: TypedValue) -> TypedValue:
        other = FloatValue(value=str(o.get_value()))

        return FloatValue(value=str(float(self.get_value()) - float(other.get_value())))

    def mul(self, o: TypedValue) -> TypedValue:
        other = FloatValue(value=str(o.get_value()))

        return FloatValue(value=str(float(self.get_value()) * float(other.get_value())))

    def truediv(self, o: TypedValue) -> TypedValue:
        other = FloatValue(value=str(o.get_value()))

        return FloatValue(value=str(float(self.get_value()) / float(other.get_value())))

    def floordiv(self, o: TypedValue) -> TypedValue:
        raise NotImplementedError("Cannot compute floor division with float")
