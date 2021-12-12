from typing import List
import typing
import unittest

from langx.opcode.opcode import OpCode
from langx.parser.node.node import Node
from langx.tokenizer.token import Token
from langx.tokenizer.tokenizer import Tokenizer
from langx.parser.parser import Parser
from langx.compiler.compiler import Compiler
from langx.decompiler.c.decompile import CDecompiler


class TestCDecompiler(unittest.TestCase):
    def __get_opcodes_from_source(self, source: str) -> List[OpCode]:
        tokens: List[Token] = Tokenizer(source=source).generate_tokens()
        ast_root: Node = Parser(tokens).parse()
        return Compiler(ast_root=ast_root).compile()

    @typing.no_type_check
    def test_null_opcodes_list(self) -> None:
        with self.assertRaises(AssertionError):
            CDecompiler(opcodes=None)

    def test_empty_opcodes_list(self) -> None:
        with self.assertRaises(AssertionError):
            CDecompiler(opcodes=[])

    def test_decompile_print_number(self) -> None:
        opcodes: List[OpCode] = self.__get_opcodes_from_source("print(1)")

        decompiled_code: List[str] = CDecompiler(opcodes=opcodes).decompile()
        expected_code: List[str] = [
            "#include <stdio.h>\n",
            "int main() {",
            '\tprintf("%d\\n", 1);',
            "\n\treturn 0; \n}",
        ]

        self.assertEqual(decompiled_code, expected_code)

    def test_decompile_print_string(self) -> None:
        opcodes: List[OpCode] = self.__get_opcodes_from_source('print("hello")')

        decompiled_code: List[str] = CDecompiler(opcodes=opcodes).decompile()
        expected_code: List[str] = [
            "#include <stdio.h>\n",
            "int main() {",
            '\tprintf("%s\\n", "hello");',
            "\n\treturn 0; \n}",
        ]

        self.assertEqual(decompiled_code, expected_code)

    def test_decompile_print_number_with_expr(self) -> None:
        opcodes: List[OpCode] = self.__get_opcodes_from_source(
            "print(1 + 2 * 3 / 4 - 5)"
        )

        decompiled_code: List[str] = CDecompiler(opcodes=opcodes).decompile()
        expected_code: List[str] = [
            "#include <stdio.h>\n",
            "int main() {",
            '\tprintf("%d\\n", 1 + 2 * 3 / 4 - 5);',
            "\n\treturn 0; \n}",
        ]

        self.assertEqual(decompiled_code, expected_code)
