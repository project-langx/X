from ..tokenizer.tokenizer import Tokenizer
from ..parser.parser import Parser
from ..utils.tree_walker import TreeWalker
from ..compiler.compiler import Compiler


def get_tokens_and_source(file_path):
    with open(file_path, "r") as f:
        source = f.read()

    tokens = Tokenizer(source).generate_tokens()
    source_lines = source.split("\n")

    source_tokens = [{"source": source_line} for source_line in source_lines]
    current_line_number = 1
    current_tokens = []
    for token in tokens:
        if token.line_num == current_line_number:
            current_tokens.append(str(token))
        else:
            source_tokens[current_line_number - 1]["tokens"] = current_tokens
            current_line_number = token.line_num
            current_tokens = [str(token)]

    return source_tokens


def get_ast_and_source(file_path):
    with open(file_path, "r") as f:
        source = f.read()

    tokens = Tokenizer(source).generate_tokens()
    ast_root = Parser(tokens).parse()
    ast = TreeWalker(ast_root).walk()

    return ast, source


def get_opcodes_and_source(file_path):
    with open(file_path, "r") as f:
        source = f.read()

    tokens = Tokenizer(source).generate_tokens()
    ast_root = Parser(tokens).parse()
    opcodes = Compiler(ast_root).compile()
    opcodes = [str(opcode) for opcode in opcodes]

    return opcodes, source
