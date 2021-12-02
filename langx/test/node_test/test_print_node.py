import unittest

from ...parser.node.print_node import PrintNode
from ...parser.node.expr_node import ExprNode
from ...parser.node.number_node import NumberNode
from ...opcode.op_type import OpType


class TestPrintNode(unittest.TestCase):
    def setUp(self):
        self.print_node = PrintNode(
            expr=ExprNode(
                expr=NumberNode(value=1, dtype="int"),
                dtype="int",
            )
        )

    def test_expr_property(self):
        self.assertEqual(self.print_node.expr.expr.value, 1)

    def test_walk_and_print(self):
        self.assertEqual(self.print_node.walk_and_print(tab_level=0),
        "PrintNode(\n\tExprNode(\n\texpr=(\n\t\tNumberNode(value=1)\n\t)\n\tdtype='int'\n\t)\n)\n")

    def test_walk_and_compile(self):
        opcodes = []
        self.print_node.walk_and_compile(opcodes)

        self.assertEqual(opcodes[0].opcode, OpType.LOAD)
        self.assertEqual(opcodes[0].op_value, 1)
        self.assertEqual(opcodes[0].op_dtype, "int")

        self.assertEqual(opcodes[1].opcode, OpType.PRINT)
        self.assertEqual(opcodes[1].op_value, "")
        self.assertEqual(opcodes[1].op_dtype, "")

