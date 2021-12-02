import unittest


from ...parser.node.string_node import StringNode
from ...opcode.op_type import OpType


class TestStringNode(unittest.TestCase):
    def setUp(self):
        self.string_node = StringNode(
            value="Hello World",
            dtype="str"
        )

    def test_value_property(self):
        self.assertEqual(self.string_node.value, "Hello World")

    def test_walk_and_print(self):
        self.assertEqual(self.string_node.walk_and_print(tab_level=0),
        "StringNode(value=Hello World)\n")

    def test_walk_and_compile(self):
        opcodes = []
        self.string_node.walk_and_compile(opcodes)

        self.assertEqual(opcodes[0].opcode, OpType.LOAD)
        self.assertEqual(opcodes[0].op_value, "Hello World")
        self.assertEqual(opcodes[0].op_dtype, "str")