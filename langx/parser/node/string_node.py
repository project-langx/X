from .node import Node


class StringNode(Node):
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    def walk_and_print(self, tab_level):
        ast_string = self._add_tabs(tab_level=tab_level)
        ast_string += f"StringNode(value={self.__value})\n"

        return ast_string