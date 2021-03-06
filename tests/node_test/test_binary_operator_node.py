import typing
import unittest
from typing import List

from langx.parser.node.binary_operator_node import BinaryOperatorNode
from langx.parser.node.number_node import NumberNode
from langx.opcode.op_type import OpType
from langx.opcode.opcode import OpCode


class TestBinaryOperatorNode(unittest.TestCase):
    def setUp(self) -> None:
        self.binary_operator_node = BinaryOperatorNode(
            operator="ADD",
            left=NumberNode(value="1", dtype="int"),
            right=NumberNode(value="2", dtype="int"),
        )

    @typing.no_type_check
    def test_null_operator(self) -> None:
        with self.assertRaises(AssertionError):
            BinaryOperatorNode(
                operator=None,
                left=NumberNode(value="1", dtype="str"),
                right=NumberNode(value="2", dtype="int"),
            )

    def test_empty_operator(self) -> None:
        with self.assertRaises(AssertionError):
            BinaryOperatorNode(
                operator="",
                left=NumberNode(value="1", dtype="int"),
                right=NumberNode(value="2", dtype="int"),
            )

    @typing.no_type_check
    def test_null_left(self) -> None:
        with self.assertRaises(AssertionError):
            BinaryOperatorNode(
                operator="ADD", left=None, right=NumberNode(value="2", dtype="int")
            )

    @typing.no_type_check
    def test_null_right(self) -> None:
        with self.assertRaises(AssertionError):
            BinaryOperatorNode(
                operator="ADD", left=NumberNode(value="1", dtype="int"), right=None
            )

    def test_operator_property(self) -> None:
        self.assertEqual(self.binary_operator_node.operator, "ADD")

    def test_left_property(self) -> None:
        self.assertEqual(
            self.binary_operator_node.left, NumberNode(value="1", dtype="int")
        )

    def test_right_property(self) -> None:
        self.assertEqual(
            self.binary_operator_node.right, NumberNode(value="2", dtype="int")
        )

    def test_eq_null_other(self) -> None:
        self.assertFalse(self.binary_operator_node == None)

    def test_eq_self_other(self) -> None:
        self.assertTrue(self.binary_operator_node == self.binary_operator_node)

    def test_eq_not_binary_operator_node(self) -> None:
        self.assertFalse(self.binary_operator_node == "")

    def test_eq_not_equal_node(self) -> None:
        self.assertFalse(
            self.binary_operator_node
            == BinaryOperatorNode(
                operator="ADD",
                left=NumberNode(value="1", dtype="int"),
                right=NumberNode(value="3", dtype="int"),
            )
        )

    def test_eq_equal_node(self) -> None:
        self.assertTrue(
            self.binary_operator_node
            == BinaryOperatorNode(
                operator="ADD",
                left=NumberNode(value="1", dtype="int"),
                right=NumberNode(value="2", dtype="int"),
            )
        )

    def test_walk_and_print(self) -> None:
        self.assertEqual(
            self.binary_operator_node.walk_and_print(tab_level=0),
            "BinaryOperatorNode(\nleft=(\n\tNumberNode(value=1, dtype='int')\n)\nop='ADD'\nright=(\n\tNumberNode(value=2, dtype='int')\n)\n",
        )

    @typing.no_type_check
    def test_walk_and_compile_null_opcodes(self) -> None:
        with self.assertRaises(AssertionError):
            self.binary_operator_node.walk_and_compile(opcodes=None)

    def test_walk_and_compile(self) -> None:
        opcodes: List[OpCode] = []
        self.binary_operator_node.walk_and_compile(opcodes)

        self.assertEqual(opcodes[0].opcode, OpType.LOAD)
        self.assertEqual(opcodes[0].op_value, "1")
        self.assertEqual(opcodes[0].op_dtype, "int")

        self.assertEqual(opcodes[1].opcode, OpType.LOAD)
        self.assertEqual(opcodes[1].op_value, "2")
        self.assertEqual(opcodes[1].op_dtype, "int")

        self.assertEqual(opcodes[2].opcode, OpType.ADD)
        self.assertEqual(opcodes[2].op_value, "")
        self.assertEqual(opcodes[2].op_dtype, "")
