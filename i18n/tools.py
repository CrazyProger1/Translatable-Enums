from i18n.types import BaseTranslatableEnum
from i18n.utils.clsutils import iter_subclasses


def extract_keys(base_enum: type[BaseTranslatableEnum] = BaseTranslatableEnum) -> set[str]:
    keys = set()
    for subenum in iter_subclasses(base_enum):
        for item in subenum:
            keys.add(item.value)
    return keys
