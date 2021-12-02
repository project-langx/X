import unittest

from ...parser.node.number_node import NumberNode
from ...opcode.op_type import OpType


class TestNumberNode(unittest.TestCase):
    def setUp(self):
        self.number_node = NumberNode(1, dtype="int")

    def test_value_property(self):
        self.assertEqual(self.number_node.value, 1)

    def test_walk_and_print(self):
        self.assertEqual(self.number_node.walk_and_print(tab_level=0), "NumberNode(value=1)\n")

    def test_walk_and_compile(self):
        opcodes = []
        self.number_node.walk_and_compile(opcodes)

        self.assertEqual(opcodes[0].opcode, OpType.LOAD)
        self.assertEqual(opcodes[0].op_value, 1)
        self.assertEqual(opcodes[0].op_dtype, "int")