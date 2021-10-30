from .node.program_node import ProgramNode
from .node.print_node import PrintNode
from ..utils.error import ParseError


class Parser:
    def __init__(self, tokens):
        self.__tokens = tokens
        
        self.__current_token = 0

    def __peek(self):
        return self.__tokens[self.__current_token]

    def __consume(self):
        self.__current_token += 1
        return self.__tokens[self.__current_token - 1]

    def __is_end(self):
        return self.__peek().type == "__eof__"

    def __expect(self, token_type):
        if self.__peek().type == token_type:
            return self.__consume()
        else:
            raise ParseError(f"Expected {token_type}, but is {self.__peek().type}!")

    def __string(self):
        string_token = self.__expect("__string__")

        return string_token.value, "string"

    def __expr(self):
        return self.__string()

    def __print(self):
        self.__expect("__print__")
        self.__expect("__left_paren__")
        expr, dtype = self.__expr()
        self.__expect("__right_paren__")
        self.__expect("__newline__")

        return PrintNode(expr=expr, dtype=dtype)

    def __single_line_statement(self):
        if self.__peek().type == '__print__':
            return self.__print()

        return self.__expr()

    def __statement(self):
        return self.__single_line_statement()

    def __program(self):
        statements = []

        while not self.__is_end():
            statements.append(self.__statement())

        return ProgramNode("<main>", statements)

    def parse(self):
        return self.__program()