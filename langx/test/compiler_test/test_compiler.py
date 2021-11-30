import unittest

from ...parser.node.program_node import ProgramNode
from ...parser.node.print_node import PrintNode
from ...parser.node.expr_node import ExprNode
from ...parser.node.string_node import StringNode
from ...parser.node.number_node import NumberNode
from ...parser.node.binary_operator_node import BinaryOperatorNode
from ...compiler.compiler import Compiler


class TestCompiler(unittest.TestCase):
    def test_simple_number_print(self) -> None:
        ast_root = ProgramNode(
            method="<main>",
            statements=[
                PrintNode(
                    expr=ExprNode(
                        expr=StringNode(value="Hello World!", dtype="str"), dtype="str"
                    )
                )
            ],
        )

        compiler = Compiler(ast_root=ast_root)
        opcodes = compiler.compile()

        self.assertEqual(len(opcodes), 2)
        self.assertEqual(str(opcodes[0]), "LOAD Hello World! str")
        self.assertEqual(str(opcodes[1]), "PRINT")

    def test_simple_number_print_with_number(self) -> None:
        ast_root = ProgramNode(
            method="<main>",
            statements=[
                PrintNode(
                    expr=ExprNode(expr=NumberNode(value="1", dtype="int"), dtype="int")
                )
            ],
        )

        compiler = Compiler(ast_root=ast_root)
        opcodes = compiler.compile()

        self.assertEqual(len(opcodes), 2)
        self.assertEqual(str(opcodes[0]), "LOAD 1 int")
        self.assertEqual(str(opcodes[1]), "PRINT")

        ast_root = ProgramNode(
            method="<main>",
            statements=[
                PrintNode(
                    expr=ExprNode(
                        expr=NumberNode(value="3.14", dtype="float"), dtype="float"
                    )
                )
            ],
        )

        compiler = Compiler(ast_root=ast_root)
        opcodes = compiler.compile()

        self.assertEqual(len(opcodes), 2)
        self.assertEqual(str(opcodes[0]), "LOAD 3.14 float")
        self.assertEqual(str(opcodes[1]), "PRINT")

    def test_expression_with_binary_operators(self) -> None:
        operators = ["ADD", "SUB", "MUL", "DIV"]

        for operator in operators:
            ast_root = ProgramNode(
                method="<main>",
                statements=[
                    PrintNode(
                        expr=ExprNode(
                            expr=BinaryOperatorNode(
                                operator=operator,
                                left=NumberNode(value="1", dtype="int"),
                                right=NumberNode(value="2", dtype="int"),
                            ),
                            dtype="int",
                        ),
                    )
                ],
            )

            compiler = Compiler(ast_root=ast_root)
            opcodes = compiler.compile()

            self.assertEqual(len(opcodes), 4)
            self.assertEqual(str(opcodes[0]), "LOAD 1 int")
            self.assertEqual(str(opcodes[1]), "LOAD 2 int")
            self.assertEqual(str(opcodes[2]), operator)
            self.assertEqual(str(opcodes[3]), "PRINT")
