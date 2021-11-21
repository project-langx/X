from .node import Node


class BinaryOperatorNode(Node):
    def __init__(self, operator, left, right):
        self.__operator = operator
        self.__left = left
        self.__right = right

    @property
    def operator(self):
        return self.__operator

    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right

    def walk_and_print(self, tab_level):
        ast_string = self._add_tabs(tab_level=tab_level)
        ast_string += f"BinaryOperatorNode(\n"
        ast_string += self._add_tabs(tab_level=tab_level)
        ast_string += f"left=(\n"

        tab_level += 1
        ast_string += self.__left.walk_and_print(tab_level)

        tab_level -= 1
        ast_string += self._add_tabs(tab_level=tab_level)
        ast_string += f")\n"

        ast_string += self._add_tabs(tab_level=tab_level)
        ast_string += f"op='{self.__operator}'\n"

        ast_string += self._add_tabs(tab_level=tab_level)
        ast_string += f"right=(\n"
        tab_level += 1

        ast_string += self.__right.walk_and_print(tab_level)

        tab_level -= 1
        ast_string += self._add_tabs(tab_level=tab_level)
        ast_string += f")\n"

        return ast_string