from typing import List

from ..parser.node.node import Node
from ..opcode.opcode import OpCode


class Compiler:
    def __init__(self, ast_root: Node) -> None:
        self.__ast_root: Node = ast_root

    def compile(self) -> List[OpCode]:
        opcodes: List[OpCode] = []
        self.__ast_root.walk_and_compile(opcodes=opcodes)

        return opcodes
