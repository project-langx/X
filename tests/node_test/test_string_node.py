import unittest
import typing
from typing import List

from langx.parser.node.string_node import StringNode
from langx.opcode.op_type import OpType
from langx.opcode.opcode import OpCode


class TestStringNode(unittest.TestCase):
    def setUp(self) -> None:
        self.string_node = StringNode(value="Hello World", dtype="str")

    @typing.no_type_check
    def test_null_value(self) -> None:
        with self.assertRaises(AssertionError):
            StringNode(value=None, dtype="str")

    @typing.no_type_check
    def test_null_dtype(self) -> None:
        with self.assertRaises(AssertionError):
            StringNode(value="Hello World", dtype=None)

    def test_value_property(self) -> None:
        self.assertEqual(self.string_node.value, "Hello World")

    def test_eq_null_other(self) -> None:
        self.assertFalse(self.string_node == None)

    def test_eq_self_other(self) -> None:
        self.assertTrue(self.string_node == self.string_node)

    def test_eq_not_binary_operator_node(self) -> None:
        self.assertFalse(self.string_node == "")

    def test_eq_not_equal_node(self) -> None:
        self.assertFalse(self.string_node == StringNode(value="Hell Worl", dtype="str"))

    def test_eq_equal_node(self) -> None:
        self.assertTrue(
            self.string_node == StringNode(value="Hello World", dtype="str")
        )

    def test_walk_and_print(self) -> None:
        self.assertEqual(
            self.string_node.walk_and_print(tab_level=0),
            "StringNode(value=Hello World)\n",
        )

    @typing.no_type_check
    def test_walk_and_compile_null_opcodes(self) -> None:
        with self.assertRaises(AssertionError):
            self.string_node.walk_and_compile(None)

    def test_walk_and_compile(self) -> None:
        opcodes: List[OpCode] = []
        self.string_node.walk_and_compile(opcodes)

        self.assertEqual(opcodes[0].opcode, OpType.LOAD)
        self.assertEqual(opcodes[0].op_value, "Hello World")
        self.assertEqual(opcodes[0].op_dtype, "str")
