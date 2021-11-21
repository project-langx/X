from .node import Node


class ExprNode(Node):
    def __init__(self, expr, dtype):
        self.__expr = expr
        self.__dtype = dtype

    @property
    def expr(self):
        return self.__expr

    @property
    def dtype(self):
        return self.__dtype

    def walk_and_print(self, tab_level):
        ast_string = self._add_tabs(tab_level=tab_level)
        ast_string += f"ExprNode(\n"
        ast_string += self._add_tabs(tab_level=tab_level)
        ast_string += f"expr=(\n"
        tab_level += 1

        ast_string += self.__expr.walk_and_print(tab_level)

        tab_level -= 1
        ast_string += self._add_tabs(tab_level=tab_level)
        ast_string += ")\n"
        ast_string += self._add_tabs(tab_level=tab_level)
        ast_string += f"dtype='{self.__dtype}'\n"
        ast_string += self._add_tabs(tab_level=tab_level)
        ast_string += f")\n"

        return ast_string

    def walk_and_compile(self, opcodes):
        self.__expr.walk_and_compile(opcodes)
