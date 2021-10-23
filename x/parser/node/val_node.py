from .node import Node


class ValNode(Node):
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @property
    def children(self):
        return None

    def __str__(self):
        return f"ValueNode(value={self.__value})"