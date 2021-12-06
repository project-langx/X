import unittest

from langx.tokenizer.tokenizer import Tokenizer
from langx.parser.parser import Parser
from langx.compiler.compiler import Compiler
from langx.decompiler.java.decompile import JavaDecompiler


class TestCDecompiler(unittest.TestCase):
    def __get_opcodes_from_source(self, source):
        tokens = Tokenizer(source).generate_tokens()
        ast = Parser(tokens).parse()
        return Compiler(ast).compile()

    def test_decompile_print_number(self):
        opcodes = self.__get_opcodes_from_source("print(1)")

        decompiled_code = JavaDecompiler(opcodes=opcodes, decompiled_file_name="Test").decompile()
        print(decompiled_code)
        self.assertEqual(decompiled_code, ['class Test {', 
        '\tpublic static void main(String[] args) {', '\t\tSystem.out.println(1);', '\t}\n}'])

    def test_decompile_print_string(self):
        opcodes = self.__get_opcodes_from_source('print("hello")')

        decompiled_code = JavaDecompiler(opcodes=opcodes, decompiled_file_name="Test").decompile()

        self.assertEqual(decompiled_code, ['class Test {', 
        '\tpublic static void main(String[] args) {', '\t\tSystem.out.println("hello");', '\t}\n}'])

    def test_decompile_print_number_with_expr(self):
        opcodes = self.__get_opcodes_from_source('print(1 + 2 * 3 / 4 - 5)')

        decompiled_code = JavaDecompiler(opcodes=opcodes, decompiled_file_name="Test").decompile()

        self.assertEqual(decompiled_code, ['class Test {', 
        '\tpublic static void main(String[] args) {', '\t\tSystem.out.println(1 + 2 * 3 / 4 - 5);', '\t}\n}'])