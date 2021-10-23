from ..utils.error import ParseError
from .node import val_node, print_node


class RecursiveDescentParser:
    def __init__(self, tokens):
        self.__tokens = tokens
        self.__root = None

    def __advance(self):
        current_tok = self.__tokens.pop(0)
        return current_tok

    def __string(self, current_tok):
        if current_tok.type == "__string__":
            return val_node.ValNode(current_tok.value)

        raise ParseError(f"Expected string")

    def __print(self, current_tok):
        token_sequence = ["__print__", "__left_paren__", "__string__", "__right_paren__"]
        string_val = ""

        for expected_token in token_sequence:
            if current_tok.type == "__string__":
                string_val = self.__string(current_tok=current_tok)
            elif current_tok.type == expected_token:
                current_tok = self.__advance()
            else:
                raise ParseError(f"Expected {expected_token}")

        return print_node.PrintNode(values=[string_val])

    def parse(self):
        current_tok = self.__advance()
        self.__root = self.__print(current_tok=current_tok)
        return self.__root