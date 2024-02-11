from i18n import (
    TranslatableEnum,
    extract_keys
)


def test_extract_keys():
    class MyEnum(TranslatableEnum):
        ONE = '1'
        TWO = '2'
        THREE = '3'
        FOUR = '4'

    assert len(extract_keys(TranslatableEnum)) == 4
