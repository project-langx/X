from typing import List

from .var_declaration_node import VarDeclNode
from .node import Node
from ...opcode.opcode import OpCode
from ...opcode.op_type import OpType



class VarAssignNode(VarDeclNode):
    def __init__(self, table_id: int, expr: Node) -> None:
        super().__init__(table_id=table_id, expr=expr)

    def walk_and_compile(self, opcodes: List[OpCode]) -> None:
        assert opcodes != None

        self.expr.walk_and_compile(opcodes=opcodes)

        opcodes.append(OpCode(opcode=OpType.ASSIGN, op_value=self.table_id, op_dtype=self.expr.dtype))

