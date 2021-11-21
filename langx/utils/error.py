class Error(Exception):
    def __init__(self, message: str) -> None:
        self.__message = message

        super().__init__(message)

    @property
    def message(self) -> str:
        return self.__message


class TokenizerError(Error):
    def __init__(self, message: str) -> None:
        super().__init__(message)

    def __str__(self) -> str:
        return f"\033[91mError:\033[m {self.message}!"


class ParseError(Error):
    def __init__(self, message: str) -> None:
        super().__init__(message)

    def __str__(self) -> str:
        return f"\033[91mError:\033[m {self.message}!"
