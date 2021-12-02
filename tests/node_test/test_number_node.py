import unittest
from typing import List

from langx.parser.node.number_node import NumberNode
from langx.opcode.op_type import OpType
from langx.opcode.opcode import OpCode


class TestNumberNode(unittest.TestCase):
    def setUp(self) -> None:
        self.number_node = NumberNode("1", dtype="int")

    def test_value_property(self) -> None:
        self.assertEqual(self.number_node.value, "1")

    def test_walk_and_print(self) -> None:
        self.assertEqual(
            self.number_node.walk_and_print(tab_level=0), "NumberNode(value=1)\n"
        )

    def test_walk_and_compile(self) -> None:
        opcodes: List[OpCode] = []
        self.number_node.walk_and_compile(opcodes)

        self.assertEqual(opcodes[0].opcode, OpType.LOAD)
        self.assertEqual(opcodes[0].op_value, "1")
        self.assertEqual(opcodes[0].op_dtype, "int")
