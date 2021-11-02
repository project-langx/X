class Error(Exception):
    def __init__(self, message):
        self.__message = message

        super().__init__(message)

    @property
    def message(self):
        return self.__message

class TokenizerError(Error):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"\033[91mError:\033[m {self.message}!"

class ParseError(Error):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"\033[91mError:\033[m {self.message}!"
