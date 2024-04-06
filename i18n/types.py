from enum import Enum
from dataclasses import dataclass
from abc import abstractmethod


class BaseTranslatableEnum(str, Enum):
    @abstractmethod
    def language(self, lang: str) -> str: ...


@dataclass(frozen=True)
class Key:
    key: str
    comment: str = None
