import unittest
from typing import List

from langx.parser.node.expr_node import ExprNode
from langx.parser.node.number_node import NumberNode
from langx.opcode.op_type import OpType
from langx.opcode.opcode import OpCode


class TestExprNode(unittest.TestCase):
    def setUp(self) -> None:
        self.expr_node = ExprNode(expr=NumberNode(value="1", dtype="int"), dtype="int")

    def test_null_expr(self):
        with self.assertRaises(AssertionError):
            ExprNode(expr=None, dtype="int")

    def test_null_dtype(self):
        with self.assertRaises(AssertionError):
            ExprNode(expr=NumberNode(value="1", dtype="int"), dtype=None)

    def test_empty_dtype(self):
        with self.assertRaises(AssertionError):
            ExprNode(expr=NumberNode(value="1", dtype="int"), dtype="")

    def test_expr_property(self) -> None:
        self.assertEqual(self.expr_node.expr, NumberNode(value="1", dtype="int"))

    def test_dtype_property(self) -> None:
        self.assertEqual(self.expr_node.dtype, "int")

    def test_walk_and_print(self) -> None:
        self.assertEqual(
            self.expr_node.walk_and_print(tab_level=0),
            "ExprNode(\nexpr=(\n\tNumberNode(value=1)\n)\ndtype='int'\n)\n",
        )

    def test_walk_and_compile_null_opcodes(self) -> None:
        with self.assertRaises(AssertionError):
            self.expr_node.walk_and_compile(None)

    def test_walk_and_compile(self) -> None:
        opcodes: List[OpCode] = []
        self.expr_node.walk_and_compile(opcodes)

        self.assertEqual(opcodes[0].opcode, OpType.LOAD)
        self.assertEqual(opcodes[0].op_value, "1")
        self.assertEqual(opcodes[0].op_dtype, "int")
