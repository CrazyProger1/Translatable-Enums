from enum import Enum

from abc import abstractmethod


class BaseTranslatableEnum(str, Enum):
    @abstractmethod
    def language(self, lang: str) -> str: ...
