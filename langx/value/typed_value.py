from abc import abstractmethod


class TypedValue:
    @abstractmethod
    def add(self, o: "TypedValue") -> "TypedValue":
        pass

    @abstractmethod
    def sub(self, o: "TypedValue") -> "TypedValue":
        pass

    @abstractmethod
    def mul(self, o: "TypedValue") -> "TypedValue":
        pass

    @abstractmethod
    def truediv(self, o: "TypedValue") -> "TypedValue":
        pass

    @abstractmethod
    def floordiv(self, o: "TypedValue") -> "TypedValue":
        pass

    @abstractmethod
    def get_value(self) -> str:
        pass
