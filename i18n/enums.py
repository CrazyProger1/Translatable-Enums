import gettext

from i18n.types import BaseTranslatableEnum
from i18n.utils.gettext import (
    language,
    get_language
)


class TranslatableEnum(BaseTranslatableEnum):
    @property
    def value(self) -> str:
        value = super(TranslatableEnum, self).value
        return gettext.gettext(value)

    def language(self, lang: str) -> str:
        with language(lang=lang):
            return self.value

    def __str__(self):
        return self.value
