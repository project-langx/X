import unittest
from typing import List

from ...parser.node.string_node import StringNode
from ...opcode.op_type import OpType
from ...opcode.opcode import OpCode


class TestStringNode(unittest.TestCase):
    def setUp(self) -> None:
        self.string_node = StringNode(value="Hello World", dtype="str")

    def test_value_property(self) -> None:
        self.assertEqual(self.string_node.value, "Hello World")

    def test_walk_and_print(self) -> None:
        self.assertEqual(
            self.string_node.walk_and_print(tab_level=0),
            "StringNode(value=Hello World)\n",
        )

    def test_walk_and_compile(self) -> None:
        opcodes: List[OpCode] = []
        self.string_node.walk_and_compile(opcodes)

        self.assertEqual(opcodes[0].opcode, OpType.LOAD)
        self.assertEqual(opcodes[0].op_value, "Hello World")
        self.assertEqual(opcodes[0].op_dtype, "str")
