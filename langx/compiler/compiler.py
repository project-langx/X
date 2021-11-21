from ..opcode.opcode import OpCode
from ..parser.node.print_node import PrintNode
from ..parser.node.number_node import NumberNode
from ..parser.node.string_node import StringNode
from ..parser.node.binary_operator_node import BinaryOperatorNode
from ..parser.node.expr_node import ExprNode
from ..opcode.op_type import OpType


class Compiler:
    def __init__(self, ast_root):
        self.__ast_root = ast_root

    def compile(self):
        opcodes = []
        self.__ast_root.walk_and_compile(opcodes)

        return opcodes
