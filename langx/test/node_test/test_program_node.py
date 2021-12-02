import unittest


from ...parser.node.program_node import ProgramNode
from ...parser.node.print_node import PrintNode
from ...parser.node.expr_node import ExprNode
from ...parser.node.number_node import NumberNode
from ...opcode.op_type import OpType


class TestProgramNode(unittest.TestCase):
    def setUp(self):
        self.program_node = ProgramNode(
            method="<main>",
            statements=[
                PrintNode(
                    expr=ExprNode(
                        expr=NumberNode(value=1, dtype="int"),
                        dtype="int",
                    )
                ),
            ]
        )

    def test_method_property(self):
        self.assertEqual(self.program_node.method, "<main>")

    def test_statements_property(self):
        self.assertEqual(len(self.program_node.statements), 1)
        self.assertEqual(self.program_node.statements[0].expr.expr.value, 1)

    def test_walk_and_print(self):
        self.assertEqual(self.program_node.walk_and_print(tab_level=0),
        "ProgramNode(method=<main>)\n\tPrintNode(\n\t\tExprNode(\n\t\texpr=(\n\t\t\tNumberNode(value=1)\n\t\t)\n\t\tdtype='int'\n\t\t)\n\t)\n")

    def test_walk_and_compile(self):
        opcodes = []
        self.program_node.walk_and_compile(opcodes)

        self.assertEqual(opcodes[0].opcode, OpType.LOAD)
        self.assertEqual(opcodes[0].op_value, 1)
        self.assertEqual(opcodes[0].op_dtype, "int")

        self.assertEqual(opcodes[1].opcode, OpType.PRINT)
        self.assertEqual(opcodes[1].op_value, "")
        self.assertEqual(opcodes[1].op_dtype, "")