from i18n.types import BaseTranslatableEnum, Key
from i18n.utils.clsutils import iter_subclasses


def extract_keys(
    base_enum: type[BaseTranslatableEnum] = BaseTranslatableEnum,
) -> set[Key]:
    keys = set()
    for subenum in iter_subclasses(base_enum):
        for item in subenum:
            keys.add(Key(key=item.value, comment=f"{subenum.__name__}.{item.name}"))
    return keys
