import unittest

from ...parser.node.expr_node import ExprNode
from ...parser.node.number_node import NumberNode
from ...opcode.op_type import OpType


class TestExprNode(unittest.TestCase):
    def setUp(self):
        self.expr_node = ExprNode(
            expr=NumberNode(value=1, dtype="int"),
            dtype="int",
        )

    def test_expr_property(self):
        self.assertEqual(self.expr_node.expr.value, 1)

    def test_dtype_property(self):
        self.assertEqual(self.expr_node.dtype, "int")

    def test_walk_and_print(self):
        self.assertEqual(self.expr_node.walk_and_print(tab_level=0), 
        "ExprNode(\nexpr=(\n\tNumberNode(value=1)\n)\ndtype='int'\n)\n")

    def test_walk_and_compile(self):
        opcodes = []
        self.expr_node.walk_and_compile(opcodes)

        self.assertEqual(opcodes[0].opcode, OpType.LOAD)
        self.assertEqual(opcodes[0].op_value, 1)
        self.assertEqual(opcodes[0].op_dtype, "int")