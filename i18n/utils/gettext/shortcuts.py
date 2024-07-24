import gettext
import os

from i18n.constants import KEY_FORMAT_VARIABLE, LANGUAGE_VARIABLE


def set_language(language: str):
    assert isinstance(language, str), "Language must be string"

    os.environ[LANGUAGE_VARIABLE] = language


def set_key_format(key_format: str):
    assert isinstance(key_format, str), "Key format must be string"

    os.environ[KEY_FORMAT_VARIABLE] = key_format


def get_language() -> str:
    return os.environ.get(LANGUAGE_VARIABLE, "en_US")


def get_key_format() -> str:
    return os.environ.get(KEY_FORMAT_VARIABLE, "{value}")


def set_domain(domain: str, localedir: str):
    gettext.bindtextdomain(domain=domain, localedir=localedir)
    gettext.textdomain(domain=domain)


def translate(key: str) -> str:
    return gettext.gettext(key)
