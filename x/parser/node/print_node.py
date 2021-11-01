class PrintNode:
    def __init__(self, expr):
        self.__expr = expr

    def __str__(self):
        return f"PrintNode(expr={self.__expr})"

    @property
    def expr(self):
        return self.__expr
