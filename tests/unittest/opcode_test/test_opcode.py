import unittest

from langx.opcode.op_type import OpType
from langx.opcode.opcode import OpCode


class TestOpCode(unittest.TestCase):
    def setUp(self) -> None:
        self.opcode_with_dtype = OpCode(OpType.LOAD, "Hello World", "string")
        self.opcode_no_dtype = OpCode(OpType.ADD, "", "")

    def test_opcode_str_with_dtype(self) -> None:
        self.assertEqual(str(self.opcode_with_dtype), "LOAD Hello World string")
        self.assertEqual(str(self.opcode_no_dtype), "ADD")

    def test_opcode_opcode_property(self) -> None:
        self.assertEqual(self.opcode_with_dtype.opcode, OpType.LOAD)
        self.assertEqual(self.opcode_no_dtype.opcode, OpType.ADD)

    def test_opcode_opvalue_property(self) -> None:
        self.assertEqual(self.opcode_with_dtype.op_value, "Hello World")
        self.assertEqual(self.opcode_no_dtype.op_value, "")

    def test_opcode_opdtype_property(self) -> None:
        self.assertEqual(self.opcode_with_dtype.op_dtype, "string")
        self.assertEqual(self.opcode_no_dtype.op_dtype, "")
