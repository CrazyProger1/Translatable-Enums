import pytest

from i18n import TranslatableEnum, set_domain, set_language


def test_translatable_enums():
    set_language('uk')
    set_domain('app', './tests/languages')

    class MyEnum(TranslatableEnum):
        HELLO = 'hello'
        WORLD = 'world'

    assert MyEnum.WORLD.value == 'Світ'


def test_translate_to_language():
    set_language('en')
    set_domain('app', './tests/languages')

    class MyEnum(TranslatableEnum):
        HELLO = 'hello'
        WORLD = 'world'

    assert MyEnum.WORLD.language('uk') == 'Світ'
    assert MyEnum.HELLO.value == 'hello'
