from .node import Node


class ProgramNode(Node):
    def __init__(self, method, statements):
        self.__method = method
        self.__statements = statements

    @property
    def method(self):
        return self.__method

    @property
    def statements(self):
        return self.__statements

    def walk_and_print(self, tab_level):
        ast_string = self._add_tabs(tab_level=tab_level)
        ast_string += f"ProgramNode(method={self.__method})\n"
        tab_level += 1

        for statement in self.__statements:
            ast_string += statement.walk_and_print(tab_level)

        return ast_string