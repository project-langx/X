from .node import Node


class PrintNode(Node):
    def __init__(self, expr):
        self.__expr = expr

    @property
    def expr(self):
        return self.__expr

    def walk_and_print(self, tab_level):
        ast_string = self._add_tabs(tab_level=tab_level)
        ast_string += f"PrintNode(\n"
        tab_level += 1

        ast_string += self.__expr.walk_and_print(tab_level)
        
        tab_level -= 1
        ast_string += self._add_tabs(tab_level=tab_level)
        ast_string += ")\n"

        return ast_string