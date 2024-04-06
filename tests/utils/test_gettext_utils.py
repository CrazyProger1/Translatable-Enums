import gettext
import os

from i18n.utils.gettext import set_language, get_language, language, set_domain


def test_set_language():
    set_language("en")

    assert os.environ["LANG"] == "en"


def test_language_contextmgr():
    set_language("en")

    with language("uk"):
        assert os.environ["LANG"] == "uk"

    assert os.environ["LANG"] == "en"


def test_set_domain():
    set_language("uk")
    set_domain("app", "./tests/languages")

    assert gettext.gettext("world") == "Світ"


def test_get_language():
    os.environ["LANG"] = "abc"

    assert get_language() == "abc"
