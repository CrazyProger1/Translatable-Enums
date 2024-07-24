from typing import Collection

from i18n.types import BaseTranslatableEnum, Key
from i18n.utils.gettext import get_key_format, language, translate


class TranslatableEnum(BaseTranslatableEnum):

    @classmethod
    @property
    def keys(cls) -> Collection[Key]:
        keys = set()
        for item in cls:
            keys.add(
                Key(
                    enum=cls,
                    name=item.name,
                    value=item.original_value,
                    comment=f"{cls.__name__}.{item.name}",
                )
            )
        return keys

    @property
    def value(self) -> str:
        key_format = get_key_format()
        item = super(TranslatableEnum, self)
        key = key_format.format(
            value=item.value,
            enum=type(self).__name__,
            name=item.name,
        )

        translation = translate(key)

        if translation == key and key_format != "{value}":
            return item.value

        return translation

    @property
    def original_value(self) -> str:
        item = super(TranslatableEnum, self)
        return item.value

    def language(self, lang: str) -> str:
        with language(lang=lang):
            return self.value

    def format(self, *args, **kwargs):
        return self.value.format(*args, **kwargs)

    def __str__(self):
        return self.value
