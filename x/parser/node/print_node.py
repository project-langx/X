from .node import Node


class PrintNode(Node):
    def __init__(self, values):
        self.__values = values

    @property
    def children(self):
        return self.__values

    def __str__(self):
        return f"PrintNode()"