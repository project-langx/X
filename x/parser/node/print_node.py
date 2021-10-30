class PrintNode:
    def __init__(self, expr, dtype):
        self.__expr = expr
        self.__dtype = dtype

    def __str__(self):
        return f"PrintNode(expr={self.__expr}, dtype='{self.__dtype}')"

    @property
    def expr(self):
        return self.__expr

    @property
    def dtype(self):
        return self.__dtype
