class ExprNode:
    def __init__(self, expr, dtype):
        self.__expr = expr
        self.__dtype = dtype

    @property
    def expr(self):
        return self.__expr

    @property
    def dtype(self):
        return self.__dtype
