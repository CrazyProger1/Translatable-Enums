from i18n.enums import TranslatableEnum
from i18n.types import BaseTranslatableEnum
from i18n.tools import extract_keys
from i18n.settings import VERSION, APP, AUTHOR
from i18n.utils.gettext import set_domain, set_language, get_language, language

__name__ = APP
__version__ = VERSION
__author__ = AUTHOR

__all__ = [
    "BaseTranslatableEnum",
    "TranslatableEnum",
    "extract_keys",
    "set_language",
    "get_language",
    "set_domain",
    "language",
]
