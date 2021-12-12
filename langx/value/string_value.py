from .typed_value import TypedValue


class StringValue(TypedValue):
    def __init__(self, value: str) -> None:
        self.__value: str = value

    def get_value(self) -> str:
        return str(self.__value)

    def add(self, o: TypedValue) -> TypedValue:
        o = StringValue(value=o.get_value())

        return StringValue(value=self.get_value() + o.get_value())

    def sub(self, o: TypedValue) -> TypedValue:
        raise NotImplementedError("Cannot compute subtraction with str")

    def mul(self, o: TypedValue) -> TypedValue:
        raise NotImplementedError("Cannot compute multiplication with str")

    def truediv(self, o: TypedValue) -> TypedValue:
        raise NotImplementedError("Cannot compute true division with str")

    def floordiv(self, o: TypedValue) -> TypedValue:
        raise NotImplementedError("Cannot compute floor division with str")
