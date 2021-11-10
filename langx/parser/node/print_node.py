class PrintNode:
    def __init__(self, expr):
        self.__expr = expr

    @property
    def expr(self):
        return self.__expr
