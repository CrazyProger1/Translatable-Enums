import pytest

from i18n import TranslatableEnum, extract_keys
from i18n.tools import save_pot
from i18n.utils.potfile import POTFile


@pytest.fixture
def test_potfile() -> str:
    return "test.pot"


class MyEnum(TranslatableEnum):
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"


def test_extract_keys():
    assert len(extract_keys(TranslatableEnum)) == 4


def test_save_pot(test_potfile):
    keys = extract_keys(TranslatableEnum)
    key_format = "{enum}.{name}.{value}"

    save_pot(test_potfile, keys=keys, key_format=key_format)

    with POTFile(test_potfile, "r") as potfile:
        result_keys = set(potfile.keys)
        assert all(
            [
                key_format.format(
                    enum=key.enum.__name__, name=key.name, value=key.value
                )
                in result_keys
                for key in keys
            ]
        )
