from typing import Any

from .op_type import OpType
from ..utils.check_class import CheckClass


class OpCode(CheckClass):
    def __init__(self, opcode: OpType, op_value: str, op_dtype: str):
        super().__init__(opcode=opcode, op_value=op_value, op_dtype=op_dtype)
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
    def op_value(self) -> str:
        return self.__op_value

    @property
    def op_dtype(self) -> str:
        return self.__op_dtype
