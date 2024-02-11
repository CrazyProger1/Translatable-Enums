from abc import ABC, abstractmethod
from enum import Enum


class BaseTranslatableEnum(str, Enum):
    pass
