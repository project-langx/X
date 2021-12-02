import unittest

from ...parser.node.number_node import NumberNode
from ...opcode.op_type import OpType


class TestNumberNode(unittest.TestCase):
    def setUp(self):
        self.number_node = NumberNode(1)

    def test_value_property(self):
        self.assertEqual(self.number_node.value, 1)

    def test_walk_and_print(self):
        print(repr(self.number_node.walk_and_print(tab_level=0)))