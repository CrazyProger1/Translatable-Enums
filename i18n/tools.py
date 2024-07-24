from typing import Iterable

from i18n.types import BaseTranslatableEnum, Key
from i18n.utils.clsutils import iter_subclasses
from i18n.utils.potfile import POTFile


def extract_keys(
    base_enum: type[BaseTranslatableEnum] = BaseTranslatableEnum,
) -> set[Key]:
    keys = set()
    for subenum in iter_subclasses(base_enum):
        keys |= subenum.keys
    return keys


def save_pot(
    file: str, keys: Iterable[Key], template: str = None, key_format: str = "{value}"
) -> None:
    with POTFile(file=file, mode="w", template=template) as potfile:
        for key in keys:
            potfile.write(
                key=key_format.format(
                    name=key.name, value=key.value, enum=key.enum.__name__
                ),
                comment=key.comment,
            )
