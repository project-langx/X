from typing import List, Tuple, Dict

from .node.node import Node
from .node.number_node import NumberNode
from .node.string_node import StringNode
from .node.binary_operator_node import BinaryOperatorNode
from .node.program_node import ProgramNode
from .node.print_node import PrintNode
from .node.expr_node import ExprNode
from .node.var_declaration_node import VarDeclNode
from .node.var_assignment_node import VarAssignNode
from .node.identifier_node import IdentifierNode
from ..utils.error import ParseError
from ..tokenizer.token import Token
from ..tokenizer.token_type import TokenType
from ..utils.check_class import CheckClass
from ..table.symbol_table import SymbolTable


class Parser(CheckClass):
    def __init__(self, tokens: List[Token], symbol_table: SymbolTable) -> None:
        super().__init__(tokens=tokens, symbol_table=symbol_table, check_empty_list=True)
        self.__tokens: List[Token] = tokens
        self.__symbol_table: SymbolTable = symbol_table

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

    def __identifier(self) -> Tuple[Node, str]:
        identifier: Token = self.__expect(TokenType.IDENTIFIER)
        table_id, dtype = self.__symbol_table.get_by_name(id_name=identifier.value)

        if table_id == None and dtype == None:
            raise ParseError(f"Undeclared variable '{identifier.value}'")

        return IdentifierNode(value=table_id, dtype=dtype), dtype

    def __term(self) -> Tuple[Node, str]:
        if self.__peek().type == TokenType.NUMBER:
            return self.__number()
        elif self.__peek().type == TokenType.IDENTIFIER:
            return self.__identifier()

        return self.__string()

    def __factor(self) -> Tuple[Node, str]:
        return self.__term()

    def __mul(self) -> Tuple[Node, str]:
        expr, dtype = self.__factor()

        op_type_to_op_type: Dict[TokenType, str] = {
            TokenType.MUL: "MUL",
            TokenType.DIV: "DIV",
        }
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

        op_type_to_op_type: Dict[TokenType, str] = {
            TokenType.ADD: "ADD",
            TokenType.SUB: "SUB",
        }
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

    def __var_declaration(self) -> Node:
        self.__expect(TokenType.VAR)
        identifier: Token = self.__expect(TokenType.IDENTIFIER)
        self.__expect(TokenType.ASSIGNMENT)
        expr: Node = self.__expr()
        
        table_id = self.__symbol_table.add(id_name=identifier.value, dtype=expr.dtype)

        return VarDeclNode(table_id=table_id, expr=expr)

    def __assign(self) -> Node:
        identifier: Token = self.__expect(TokenType.IDENTIFIER)
        self.__expect(TokenType.ASSIGNMENT)
        expr: Node = self.__expr()

        table_id = self.__symbol_table.update(id_name=identifier.value, dtype=expr.dtype)

        return VarAssignNode(table_id=table_id, expr=expr)

    def __single_line_statement(self) -> Node:
        if self.__peek().type == TokenType.PRINT:
            print_node: Node = self.__print()
            self.__expect(TokenType.NEWLINE)
            return print_node
        elif self.__peek().type == TokenType.VAR:
            var_decl_node: Node = self.__var_declaration()
            self.__expect(TokenType.NEWLINE)
            return var_decl_node
        elif self.__peek().type == TokenType.IDENTIFIER:
            assign_node: Node = self.__assign()
            self.__expect(TokenType.NEWLINE)
            return assign_node

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
