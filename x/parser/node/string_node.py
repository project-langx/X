class StringNode:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    def __str__(self):
        return f"StringNode(value={self.__value})"