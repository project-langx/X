from typing import List, Tuple

from ..utils.error import TokenizerError
from .token import Token


class Tokenizer:
    def __init__(self, source: str) -> None:
        self.__source: str = source
        self.__line_num: int = 1
        self.__pointer: int = 0
        self.__lexeme: str = ""

        self.__tokens: List[Token] = []

    def __is_keyword(self) -> str:
        while self.__source[self.__pointer].isalpha():
            self.__lexeme += self.__source[self.__pointer]
            self.__pointer += 1
        self.__pointer -= 1

        if self.__lexeme == "print":
            return "__print__"

        return ""

    def __is_string(self) -> str:
        self.__pointer += 1
        while self.__source[self.__pointer] != '"':
            self.__lexeme += self.__source[self.__pointer]
            self.__pointer += 1

        return "__string__"

    def __is_number(self) -> Tuple[str, str]:
        is_float: bool = False
        while (
            self.__source[self.__pointer].isdigit()
            or self.__source[self.__pointer] == "."
        ):
            self.__lexeme += self.__source[self.__pointer]
            self.__pointer += 1

        self.__pointer -= 1

        if self.__lexeme.count(".") > 1:
            raise TokenizerError(
                message="A number cannot have more than one decimal points!"
            )

        if self.__lexeme.count(".") == 1:
            is_float = True

        return "__number__", "float" if is_float else "int"

    def __operator(self) -> str:
        if self.__source[self.__pointer] == "+":
            return "__add__"
        elif self.__source[self.__pointer] == "-":
            return "__sub__"
        elif self.__source[self.__pointer] == "*":
            return "__mul__"
        elif self.__source[self.__pointer] == "/":
            return "__div__"

        return ""

    def generate_tokens(self) -> List[Token]:
        while self.__pointer < len(self.__source):
            self.__lexeme = ""
            if self.__source[self.__pointer].isalpha():
                self.__tokens.append(
                    Token(self.__is_keyword(), "", self.__lexeme, self.__line_num)
                )
            elif self.__source[self.__pointer] == "(":
                self.__tokens.append(Token("__left_paren__", "", "", self.__line_num))
            elif self.__source[self.__pointer] == ")":
                self.__tokens.append(Token("__right_paren__", "", "", self.__line_num))
            elif self.__source[self.__pointer] in ["+", "-", "*", "/"]:
                operator = self.__operator()
                self.__tokens.append(
                    Token(operator, "", self.__source[self.__pointer], self.__line_num)
                )
            elif self.__source[self.__pointer] == '"':
                self.__tokens.append(
                    Token(self.__is_string(), "string", self.__lexeme, self.__line_num)
                )
            elif self.__source[self.__pointer].isdigit():
                number, dtype = self.__is_number()
                self.__tokens.append(
                    Token(number, dtype, self.__lexeme, self.__line_num)
                )
            elif self.__source[self.__pointer] == "\n":
                self.__line_num += 1
                self.__tokens.append(Token("__newline__", "", "", self.__line_num - 1))

            self.__pointer += 1

        self.__tokens.append(Token("__newline__", "", "", self.__line_num))
        self.__tokens.append(Token("__eof__", "", "", self.__line_num + 1))

        return self.__tokens
