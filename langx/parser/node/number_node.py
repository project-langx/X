from typing import List

from .node import Node
from ...opcode.opcode import OpCode
from ...opcode.op_type import OpType


class NumberNode(Node):
    def __init__(self, value: str, dtype: str) -> None:
        self.__value: str = value
        self.__dtype: str = dtype

    @property
    def value(self) -> str:
        return self.__value

    def __eq__(self, __o: object) -> bool:
        if self is __o:
            return True

        if not isinstance(__o, NumberNode):
            return False

        return self.value == __o.value

    def walk_and_print(self, tab_level: int) -> str:
        ast_string: str = self._add_tabs(tab_level=tab_level)
        ast_string += f"NumberNode(value={self.__value})\n"

        return ast_string

    def walk_and_compile(self, opcodes: List[OpCode]) -> None:
        opcodes.append(
            OpCode(opcode=OpType.LOAD, op_value=self.__value, op_dtype=self.__dtype)
        )
