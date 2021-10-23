from .node import Node


class ValNode(Node):
    def __init__(self, value, type):
        self.__value = value
        self.__type = type

    @property
    def value(self):
        return self.__value

    @property
    def type(self):
        return self.__type

    @property
    def children(self):
        return None

    def __str__(self):
        return f"ValueNode(value={self.__value}, type={self.__type})"