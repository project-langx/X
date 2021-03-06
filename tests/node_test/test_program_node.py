import typing
import unittest
from typing import List

from langx.parser.node.program_node import ProgramNode
from langx.parser.node.print_node import PrintNode
from langx.parser.node.expr_node import ExprNode
from langx.parser.node.number_node import NumberNode
from langx.opcode.op_type import OpType
from langx.opcode.opcode import OpCode


class TestProgramNode(unittest.TestCase):
    def setUp(self) -> None:
        self.program_node = ProgramNode(
            method="<main>",
            statements=[
                PrintNode(
                    expr=ExprNode(expr=NumberNode(value="1", dtype="int"), dtype="int",)
                ),
            ],
        )

    @typing.no_type_check
    def test_null_method(self) -> None:
        with self.assertRaises(AssertionError):
            ProgramNode(
                method=None,
                statements=[
                    PrintNode(
                        expr=ExprNode(
                            expr=NumberNode(value="1", dtype="int"), dtype="int",
                        )
                    ),
                ],
            )

    def test_empty_method(self) -> None:
        with self.assertRaises(AssertionError):
            ProgramNode(
                method="",
                statements=[
                    PrintNode(
                        expr=ExprNode(
                            expr=NumberNode(value="1", dtype="int"), dtype="int",
                        )
                    ),
                ],
            )

    @typing.no_type_check
    def test_null_statements_list(self) -> None:
        with self.assertRaises(AssertionError):
            ProgramNode(method="<main>", statements=None)

    def test_empty_statements_list(self) -> None:
        with self.assertRaises(AssertionError):
            ProgramNode(method="<main>", statements=[])

    def test_method_property(self) -> None:
        self.assertEqual(self.program_node.method, "<main>")

    def test_statements_property(self) -> None:
        self.assertEqual(len(self.program_node.statements), 1)

        expected_statements = [
            PrintNode(
                expr=ExprNode(expr=NumberNode(value="1", dtype="int"), dtype="int",)
            )
        ]

        for statement, expected_statement in zip(
            self.program_node.statements, expected_statements
        ):
            self.assertEqual(statement, expected_statement)

    def test_eq_null_other(self) -> None:
        self.assertFalse(self.program_node == None)

    def test_eq_self_other(self) -> None:
        self.assertTrue(self.program_node == self.program_node)

    def test_eq_not_binary_operator_node(self) -> None:
        self.assertFalse(self.program_node == "")

    def test_eq_not_equal_node(self) -> None:
        self.assertFalse(
            self.program_node
            == ProgramNode(
                method="<mai>",
                statements=[
                    PrintNode(
                        expr=ExprNode(
                            expr=NumberNode(value="1", dtype="int"), dtype="int",
                        )
                    ),
                ],
            )
        )

    def test_eq_equal_node(self) -> None:
        self.assertTrue(
            self.program_node
            == ProgramNode(
                method="<main>",
                statements=[
                    PrintNode(
                        expr=ExprNode(
                            expr=NumberNode(value="1", dtype="int"), dtype="int",
                        )
                    ),
                ],
            )
        )

    def test_walk_and_print(self) -> None:
        self.assertEqual(
            self.program_node.walk_and_print(tab_level=0),
            "ProgramNode(method=<main>)\n\tPrintNode(\n\t\tExprNode(\n\t\texpr=(\n\t\t\tNumberNode(value=1, dtype='int')\n\t\t)\n\t\tdtype='int'\n\t\t)\n\t)\n",
        )

    @typing.no_type_check
    def test_walk_and_compile_null_opcodes(self) -> None:
        with self.assertRaises(AssertionError):
            self.program_node.walk_and_compile(None)

    def test_walk_and_compile(self) -> None:
        opcodes: List[OpCode] = []
        self.program_node.walk_and_compile(opcodes)

        self.assertEqual(opcodes[0].opcode, OpType.LOAD)
        self.assertEqual(opcodes[0].op_value, "1")
        self.assertEqual(opcodes[0].op_dtype, "int")

        self.assertEqual(opcodes[1].opcode, OpType.PRINT)
        self.assertEqual(opcodes[1].op_value, "")
        self.assertEqual(opcodes[1].op_dtype, "")
