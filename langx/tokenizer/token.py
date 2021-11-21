from typing import NamedTuple


class Token(NamedTuple):
    type: str
    dtype: str
    value: str
    line_num: int