import typing
import unittest
from typing import List

from langx.parser.node.print_node import PrintNode
from langx.parser.node.expr_node import ExprNode
from langx.parser.node.number_node import NumberNode
from langx.opcode.op_type import OpType
from langx.opcode.opcode import OpCode


class TestPrintNode(unittest.TestCase):
    def setUp(self) -> None:
        self.print_node = PrintNode(
            expr=ExprNode(expr=NumberNode(value="1", dtype="int"), dtype="int",)
        )

    @typing.no_type_check
    def test_null_expr(self) -> None:
        with self.assertRaises(AssertionError):
            PrintNode(expr=None)

    def test_expr_property(self) -> None:
        self.assertEqual(
            self.print_node.expr,
            ExprNode(expr=NumberNode(value="1", dtype="int"), dtype="int",),
        )

    def test_eq_null_other(self) -> None:
        self.assertFalse(self.print_node == None)

    def test_eq_self_other(self) -> None:
        self.assertTrue(self.print_node == self.print_node)

    def test_eq_not_binary_operator_node(self) -> None:
        self.assertFalse(self.print_node == "")

    def test_eq_not_equal_node(self) -> None:
        self.assertFalse(
            self.print_node
            == PrintNode(
                expr=ExprNode(expr=NumberNode(value="2", dtype="int"), dtype="int",)
            )
        )

    def test_eq_equal_node(self) -> None:
        self.assertTrue(
            self.print_node
            == PrintNode(
                expr=ExprNode(expr=NumberNode(value="1", dtype="int"), dtype="int",)
            )
        )

    def test_walk_and_print(self) -> None:
        self.assertEqual(
            self.print_node.walk_and_print(tab_level=0),
            "PrintNode(\n\tExprNode(\n\texpr=(\n\t\tNumberNode(value=1, dtype='int')\n\t)\n\tdtype='int'\n\t)\n)\n",
        )

    @typing.no_type_check
    def test_walk_and_compile_null_opcodes(self) -> None:
        with self.assertRaises(AssertionError):
            self.print_node.walk_and_compile(None)

    def test_walk_and_compile(self) -> None:
        opcodes: List[OpCode] = []
        self.print_node.walk_and_compile(opcodes)

        self.assertEqual(opcodes[0].opcode, OpType.LOAD)
        self.assertEqual(opcodes[0].op_value, "1")
        self.assertEqual(opcodes[0].op_dtype, "int")

        self.assertEqual(opcodes[1].opcode, OpType.PRINT)
        self.assertEqual(opcodes[1].op_value, "")
        self.assertEqual(opcodes[1].op_dtype, "")
