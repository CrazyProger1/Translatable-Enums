from i18n.types import BaseTranslatableEnum
from i18n.utils.gettext import language, translate


class TranslatableEnum(BaseTranslatableEnum):

    @property
    def value(self) -> str:
        item = super(TranslatableEnum, self)
        return translate(item.value)

    def language(self, lang: str) -> str:
        with language(lang=lang):
            return self.value

    def format(self, *args, **kwargs):
        return self.value.format(*args, **kwargs)

    def __str__(self):
        return self.value
