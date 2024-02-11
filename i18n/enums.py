import gettext

from i18n.types import BaseTranslatableEnum


class TranslatableEnum(BaseTranslatableEnum):
    @property
    def value(self) -> str:
        value = super(TranslatableEnum, self).value
        return gettext.gettext(value)

    def __str__(self):
        return self.value
