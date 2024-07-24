from abc import abstractmethod
from dataclasses import dataclass
from enum import Enum


class BaseTranslatableEnum(str, Enum):
    @abstractmethod
    def language(self, lang: str) -> str: ...


@dataclass(frozen=True)
class Key:
    enum: BaseTranslatableEnum
    name: str
    value: str
    comment: str = None
