from enum import Enum


class BaseTranslatableEnum(str, Enum):
    def language(self, lang: str) -> str:
        raise NotImplementedError
