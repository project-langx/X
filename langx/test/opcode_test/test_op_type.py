import unittest

from ...opcode.op_type import OpType


class TestOpType(unittest.TestCase):
    def test_op_type_print(self) -> None:
        self.assertEqual(OpType.PRINT.value, 0)
        self.assertEqual(OpType.PRINT.name, "PRINT")
