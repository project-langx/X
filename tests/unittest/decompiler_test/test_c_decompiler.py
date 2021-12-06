import unittest

from langx.tokenizer.tokenizer import Tokenizer
from langx.parser.parser import Parser
from langx.compiler.compiler import Compiler
from langx.decompiler.c.decompile import CDecompiler


class TestCDecompiler(unittest.TestCase):
    def __get_opcodes_from_source(self, source):
        tokens = Tokenizer(source).generate_tokens()
        ast = Parser(tokens).parse()
        return Compiler(ast).compile()

    def test_decompile_print_number(self):
        opcodes = self.__get_opcodes_from_source("print(1)")

        decompiled_code = CDecompiler(opcodes=opcodes).decompile()

        self.assertEqual(decompiled_code, ['#include <stdio.h>\n', 
        'int main() {', '\tprintf("%d\\n", 1);', '\n\treturn 0; \n}'])

    def test_decompile_print_string(self):
        opcodes = self.__get_opcodes_from_source('print("hello")')

        decompiled_code = CDecompiler(opcodes=opcodes).decompile()

        self.assertEqual(decompiled_code, ['#include <stdio.h>\n', 
        'int main() {', '\tprintf("%s\\n", "hello");', '\n\treturn 0; \n}'])

    def test_decompile_print_number_with_expr(self):
        opcodes = self.__get_opcodes_from_source('print(1 + 2 * 3 / 4 - 5)')

        decompiled_code = CDecompiler(opcodes=opcodes).decompile()

        self.assertEqual(decompiled_code, ['#include <stdio.h>\n', 
        'int main() {', '\tprintf("%d\\n", 1 + 2 * 3 / 4 - 5);', '\n\treturn 0; \n}'])