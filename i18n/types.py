from abc import abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Collection


class BaseTranslatableEnum(str, Enum):
    @classmethod
    @property
    @abstractmethod
    def keys(cls) -> Collection["Key"]: ...

    @property
    @abstractmethod
    def original_value(self) -> str: ...

    @abstractmethod
    def language(self, lang: str) -> str: ...


@dataclass(frozen=True)
class Key:
    enum: BaseTranslatableEnum
    name: str
    value: str
    comment: str = None
