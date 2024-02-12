from typing import Literal, NewType

TextFileMode = NewType('TextFileMode', Literal['r', 'w', 'a'])
