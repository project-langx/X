from abc import abstractmethod
from typing import List

from ...opcode.opcode import OpCode


class Node:
    @abstractmethod
    def walk_and_print(self, tab_level: int) -> str:
        pass

    @abstractmethod
    def walk_and_compile(self, opcodes: List[OpCode]) -> None:
        pass

    def _add_tabs(self, tab_level: int) -> str:
        return "\t" * tab_level
