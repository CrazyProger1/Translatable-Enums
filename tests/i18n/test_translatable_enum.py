import pytest

from i18n import TranslatableEnum


def test():
    class MyEnum(TranslatableEnum):
        HELLO = 'hello'
        WORLD = 'world'

    print(MyEnum.HELLO)
