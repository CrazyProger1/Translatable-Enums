import gettext
import os


def set_language(language: str):
    assert isinstance(language, str), 'Language must be string'

    os.environ['LANG'] = language


def get_language() -> str:
    return os.environ.get('LANG', 'en_US')


def set_domain(domain: str, localedir: str):
    gettext.bindtextdomain(
        domain=domain,
        localedir=localedir
    )
    gettext.textdomain(domain=domain)
