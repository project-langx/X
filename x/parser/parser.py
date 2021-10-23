from ..utils.error import ParseError
from .node import val_node, print_node


class RecursiveDescentParser:
    def __init__(self, tokens):
        self.__tokens = tokens

        self.__root = None
        self.__current_tok = None

    def __advance(self):
        current_tok = self.__tokens.pop(0)
        return current_tok

    def __string(self):
        if self.__current_tok.type == "__string__":
            return val_node.ValNode(self.__current_tok.value)

        raise ParseError(f"Expected string")

    def __number(self):
        if self.__current_tok.type == "__number__":
            return val_node.ValNode(self.__current_tok.value)

        raise ParseError(f"Expected number")

    def __print(self):
        token_sequence = ["__print__", "__left_paren__", ["__string__", "__number__"], "__right_paren__"]
        string_val = ""

        for expected_token in token_sequence:
            if self.__current_tok.type == "__string__":
                string_val = self.__string()
                self.__current_tok = self.__advance()
            elif self.__current_tok.type == "__number__":
                string_val = self.__number()
                self.__current_tok = self.__advance()
            elif self.__current_tok.type == expected_token:
                self.__current_tok = self.__advance()
            else:
                raise ParseError(f"Expected {expected_token}")

        return print_node.PrintNode(values=[string_val])

    def parse(self):
        self.__current_tok = self.__advance()
        trees = []

        while self.__current_tok.type != "__eof__":
            self.__root = self.__print()
            trees.append(self.__root)
            self.__current_tok = self.__advance()

        return trees