from typing import List

from ..parser.node.node import Node
from ..opcode.opcode import OpCode
from ..utils.check_class import CheckClass


class Compiler(CheckClass):
    def __init__(self, ast_root: Node) -> None:
        super().__init__(ast_root=ast_root)
        self.__ast_root: Node = ast_root

    def compile(self) -> List[OpCode]:
        opcodes: List[OpCode] = []
        self.__ast_root.walk_and_compile(opcodes=opcodes)

        return opcodes
