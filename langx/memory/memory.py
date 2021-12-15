from typing import Dict, Optional

from ..value.value import Value


class Memory:
    def __init__(self) -> None:
        self.__memory: Dict[int, str] = {}

    def push_to_memory(self, memory_location: int, value: Value) -> None:
        self.__memory[memory_location] = value

    def get_from_memory(self, memory_location: int) -> Optional[Value]:
        return self.__memory.get(memory_location)

    def remove_from_memory(self, memory_location: int) -> None:
        if memory_location in self.__memory:
            del self.__memory[memory_location]

    def __str__(self) -> str:
        memory_str: str = ""

        for memory_location, value in self.__memory.items():
            memory_str += f"{memory_location}: {value.value}"

        return memory_str