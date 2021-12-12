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

    def test_null_expr(self):
        with self.assertRaises(AssertionError):
            PrintNode(expr=None)

    def test_expr_property(self) -> None:
        self.assertEqual(
            self.print_node.expr,
            ExprNode(expr=NumberNode(value="1", dtype="int"), dtype="int",),
        )

    def test_walk_and_print(self) -> None:
        self.assertEqual(
            self.print_node.walk_and_print(tab_level=0),
            "PrintNode(\n\tExprNode(\n\texpr=(\n\t\tNumberNode(value=1)\n\t)\n\tdtype='int'\n\t)\n)\n",
        )

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