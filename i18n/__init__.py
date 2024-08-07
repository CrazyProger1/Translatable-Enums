from i18n.enums import TranslatableEnum
from i18n.settings import APP, AUTHOR, VERSION
from i18n.tools import extract_keys
from i18n.types import BaseTranslatableEnum
from i18n.utils.gettext import (
    get_key_format,
    get_language,
    language,
    set_domain,
    set_key_format,
    set_language,
)

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
    "get_key_format",
    "set_key_format",
]
