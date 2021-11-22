from typing import Any

from .op_type import OpType


class OpCode:
    def __init__(self, opcode: OpType, op_value: Any, op_dtype: str):
        self.__opcode: OpType = opcode
        self.__op_value: str = op_value
        self.__op_dtype: str = op_dtype

    def __str__(self) -> str:
        opcode: str = str(self.__opcode)
        opcode = opcode.split(".")[1]

        if self.__op_value == "" and self.__op_dtype == "":
            return str(self.__opcode).split(".")[1]

        return f"{opcode} {self.__op_value} {self.__op_dtype}"

    @property
    def opcode(self) -> OpType:
        return self.__opcode

    @property
    def op_value(self) -> Any:
        return self.__op_value

    @property
    def op_dtype(self) -> str:
        return self.__op_dtype
