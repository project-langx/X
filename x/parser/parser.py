from .node.number_node import NumberNode
from .node.string_node import StringNode
from .node.binary_operator_node import BinaryOperatorNode
from .node.program_node import ProgramNode
from .node.print_node import PrintNode
from .node.expr_node import ExprNode
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

        return StringNode(value=string_token.value), "string"

    def __number(self):
        number_token = self.__expect("__number__")

        return NumberNode(value=number_token.value), number_token.dtype

    def __term(self):
        if self.__peek().type == "__number__":
            return self.__number()

        return self.__string()

    def __factor(self):
        return self.__term()

    def __mul(self):
        expr, dtype = self.__factor()

        op_type_to_op_type = {"__mul__": "MUL", "__div__": "DIV"}
        while self.__peek().type in ["__mul__", "__div__"]:
            op = self.__consume()
            right_expr, right_dtype = self.__mul()

            if dtype != right_dtype:
                raise ParseError(f"Type mismatch: {dtype} and {right_dtype}")

            expr = BinaryOperatorNode(operator=op_type_to_op_type[op.type], left=expr, right=right_expr)

        return expr, dtype

    def __sum(self):
        expr, dtype = self.__mul()

        op_type_to_op_type = {"__add__": "ADD", "__sub__": "SUB"}
        while self.__peek().type in ["__add__", "__sub__"]:
            op = self.__consume()
            right_expr, right_dtype = self.__mul()

            if dtype != right_dtype:
                raise ParseError(f"Type mismatch: {dtype} and {right_dtype}")

            expr = BinaryOperatorNode(operator=op_type_to_op_type[op.type], left=expr, right=right_expr)

        return expr, dtype

    def __expr(self):
        expr, dtype = self.__sum()
        return ExprNode(expr=expr, dtype=dtype)

    def __print(self):
        self.__expect("__print__")
        self.__expect("__left_paren__")
        expr = self.__expr()
        self.__expect("__right_paren__")

        return PrintNode(expr=expr)

    def __single_line_statement(self):
        if self.__peek().type == "__print__":
            print_node = self.__print()
            self.__expect("__newline__")
            return print_node

        raise ParseError(f"Empty expressions are not allowed")

    def __statement(self):
        return self.__single_line_statement()

    def __program(self):
        statements = []

        while not self.__is_end():
            statements.append(self.__statement())

        return ProgramNode("<main>", statements)

    def parse(self):
        return self.__program()
