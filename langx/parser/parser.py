from typing import List, Tuple, Dict

from .node.node import Node
from .node.number_node import NumberNode
from .node.string_node import StringNode
from .node.binary_operator_node import BinaryOperatorNode
from .node.program_node import ProgramNode
from .node.print_node import PrintNode
from .node.expr_node import ExprNode
from ..utils.error import ParseError
from ..tokenizer.token import Token
from ..tokenizer.token_type import TokenType


class Parser:
    def __init__(self, tokens: List[Token]) -> None:
        self.__tokens: List[Token] = tokens

        self.__current_token: int = 0

    def __peek(self) -> Token:
        return self.__tokens[self.__current_token]

    def __consume(self) -> Token:
        self.__current_token += 1
        return self.__tokens[self.__current_token - 1]

    def __is_end(self) -> bool:
        return self.__peek().type == TokenType.EOF

    def __expect(self, token_type: TokenType) -> Token:
        if self.__peek().type == token_type:
            return self.__consume()
        else:
            raise ParseError(f"Expected {token_type}, but is {self.__peek().type}!")

    def __string(self) -> Tuple[Node, str]:
        string_token = self.__expect(TokenType.STRING)

        return StringNode(value=string_token.value, dtype="string"), "string"

    def __number(self) -> Tuple[Node, str]:
        number_token = self.__expect(TokenType.NUMBER)

        return (
            NumberNode(value=number_token.value, dtype=number_token.dtype),
            number_token.dtype,
        )

    def __term(self) -> Tuple[Node, str]:
        if self.__peek().type == TokenType.NUMBER:
            return self.__number()

        return self.__string()

    def __factor(self) -> Tuple[Node, str]:
        return self.__term()

    def __mul(self) -> Tuple[Node, str]:
        expr, dtype = self.__factor()

        op_type_to_op_type: Dict[TokenType, str] = {TokenType.MUL: "MUL", TokenType.DIV: "DIV"}
        while self.__peek().type in [TokenType.MUL, TokenType.DIV]:
            op: Token = self.__consume()
            right_expr, right_dtype = self.__mul()

            if dtype != right_dtype:
                raise ParseError(f"Type mismatch: {dtype} and {right_dtype}")

            expr = BinaryOperatorNode(
                operator=op_type_to_op_type[op.type], left=expr, right=right_expr
            )

        return expr, dtype

    def __sum(self) -> Tuple[Node, str]:
        expr, dtype = self.__mul()

        op_type_to_op_type: Dict[TokenType, str] = {TokenType.ADD: "ADD", TokenType.SUB: "SUB"}
        while self.__peek().type in [TokenType.ADD, TokenType.SUB]:
            op: Token = self.__consume()
            right_expr, right_dtype = self.__mul()

            if dtype != right_dtype:
                raise ParseError(f"Type mismatch: {dtype} and {right_dtype}")

            expr = BinaryOperatorNode(
                operator=op_type_to_op_type[op.type], left=expr, right=right_expr
            )

        return expr, dtype

    def __expr(self) -> Node:
        expr, dtype = self.__sum()
        return ExprNode(expr=expr, dtype=dtype)

    def __print(self) -> Node:
        self.__expect(TokenType.PRINT)
        self.__expect(TokenType.LEFT_PAREN)
        expr: Node = self.__expr()
        self.__expect(TokenType.RIGHT_PAREN)

        return PrintNode(expr=expr)

    def __single_line_statement(self) -> Node:
        if self.__peek().type == TokenType.PRINT:
            print_node: Node = self.__print()
            self.__expect(TokenType.NEWLINE)
            return print_node

        raise ParseError("Empty expressions are not allowed")

    def __statement(self) -> Node:
        return self.__single_line_statement()

    def __program(self) -> Node:
        statements: List[Node] = []

        while not self.__is_end():
            statements.append(self.__statement())

        return ProgramNode("<main>", statements)

    def parse(self) -> Node:
        return self.__program()
