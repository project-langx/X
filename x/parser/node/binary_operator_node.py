class BinaryOperatorNode:
    def __init__(self, operator, left, right):
        self.__operator = operator
        self.__left = left
        self.__right = right

    @property
    def operator(self):
        return self.__operator

    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right