from typing import List

from ...opcode.opcode import OpCode
from ...opcode.op_type import OpType
from ...utils.check_class import CheckClass
from .node import Node


class VarDeclNode(CheckClass, Node):
    def __init__(self, table_id: int, expr: Node) -> None:
        super().__init__()

        self.__table_id: int = table_id
        self.__expr: Node = expr

    @property
    def table_id(self) -> int:
        return self.__table_id

    @property
    def expr(self) -> Node:
        return self.__expr

    def __eq__(self, __o: object) -> bool:
        if __o == None:
            return False

        if self is __o:
            return True

        if not isinstance(__o, VarDeclNode):
            return False

        return (
            self.table_id == __o.table_id
            and self.expr == __o.expr
        )

    def walk_and_print(self, tab_level: int) -> str:
        ast_string: str = self._add_tabs(tab_level=tab_level)
        ast_string += "VarDeclNode(\n"
        ast_string += self._add_tabs(tab_level=tab_level)
        ast_string += f"table_id={self.table_id}\n"

        ast_string += self._add_tabs(tab_level=tab_level)
        ast_string += f"expr={self.table_id}(\n"

        tab_level += 1
        ast_string += self.__expr.walk_and_print(tab_level=tab_level)

        tab_level -= 1
        ast_string += self._add_tabs(tab_level=tab_level)
        ast_string += ")\n"

        return ast_string

    def walk_and_compile(self, opcodes: List[OpCode]) -> None:
        assert opcodes != None

        self.__expr.walk_and_compile(opcodes=opcodes)

        opcodes.append(OpCode(opcode=OpType.VAR, op_value=self.table_id, op_dtype=self.__expr.dtype))