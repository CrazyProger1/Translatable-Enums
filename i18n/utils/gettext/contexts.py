from contextlib import contextmanager

from .shortcuts import (
    get_language,
    set_language
)


@contextmanager
def language(lang: str):
    actual_lang = get_language()

    try:
        set_language(lang)
        yield
    finally:
        set_language(actual_lang)
