from typing import List

from ...utils.check_class import CheckClass
from .node import Node
from ...opcode.opcode import OpCode
from ...opcode.op_type import OpType


class IdentifierNode(CheckClass, Node):
    def __init__(self, value: int, dtype: str) -> None:
        super().__init__(value=value, dtype=dtype, check_empty_str=True)

        self.__value: int = value
        self.__dtype: str = dtype

    @property
    def value(self) -> int:
        return self.__value

    def __eq__(self, __o: object) -> bool:
        if __o == None:
            return False

        if self is __o:
            return True

        if not isinstance(__o, IdentifierNode):
            return False

        return (self.value == __o.value and self.dtype == __o.dtype)

    def walk_and_print(self, tab_level: int) -> str:
        ast_string: str = self._add_tabs(tab_level=tab_level)
        ast_string += f"IdentifierNode(value={self.__value}, dtype='{self.__dtype}')\n"

        return ast_string

    def walk_and_compile(self, opcodes: List[OpCode]) -> None:
        assert opcodes != None

        opcodes.append(
            OpCode(opcode=OpType.LOAD_VAR, op_value=self.__value, op_dtype=self.__dtype)
        )