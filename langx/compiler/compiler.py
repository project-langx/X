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

        self.__opcodes = []

    def __check_expr_type_and_walk(self, node, dtype):
        if type(node) is NumberNode:
            self.__walk_number(node=node, dtype=dtype)
        elif type(node) is StringNode:
            self.__walk_string(node=node, dtype=dtype)
        elif type(node) is BinaryOperatorNode:
            self.__walk_binary_operator(node=node, dtype=dtype)

    def __walk_number(self, node, dtype):
        self.__opcodes.append(OpCode(opcode=OpType.LOAD, op_value=node.value, op_dtype=dtype))

    def __walk_string(self, node, dtype):
        self.__opcodes.append(OpCode(opcode=OpType.LOAD, op_value=node.value, op_dtype=dtype))

    def __walk_binary_operator(self, node, dtype):
        self.__check_expr_type_and_walk(node=node.left, dtype=dtype)
        self.__check_expr_type_and_walk(node=node.right, dtype=dtype)

        self.__opcodes.append(OpCode(opcode=OpType[node.operator], op_value="", op_dtype=""))

    def __walk_expr(self, node):
        self.__check_expr_type_and_walk(node=node.expr, dtype=node.dtype)

    def __walk_print(self, node):
        self.__walk_expr(node=node.expr)

        self.__opcodes.append(OpCode(opcode=OpType.PRINT, op_value="", op_dtype=""))

    def __walk_program(self, node):
        for statement in node.statements:
            if type(statement) is PrintNode:
                self.__walk_print(node=statement)

    def compile(self):
        self.__walk_program(node=self.__ast_root)

        return self.__opcodes
