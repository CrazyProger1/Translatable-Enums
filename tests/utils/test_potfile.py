import pytest
import re

from i18n.utils.potfile import POTFile


@pytest.fixture
def file():
    return "tests/utils/test.pot"


@pytest.fixture
def keys():
    return {"test1", "test2", "test3"}


@pytest.fixture
def template():
    return "Template"


@pytest.fixture
def create_potfile(file, keys):
    with open(file=file, mode="w") as f:
        for key in keys:
            f.write(f'msgid "{key}"\nmsgstr ""\n')


def test_iter_messages(create_potfile, file, keys):
    with POTFile(file, "r") as potfile:
        for message1, message2 in zip(potfile.keys, potfile):
            assert message1 == message2
            keys.remove(message1)

    assert len(keys) == 0


def test_add_keys(file, keys):
    with POTFile(file, "w") as potfile:
        for key in keys:
            potfile.write(key=key)

    with POTFile(file, "r") as potfile:
        for message in potfile:
            keys.remove(message)

    assert len(keys) == 0


def test_template(file, template):
    with POTFile(file, mode="w", template=template):
        pass

    with open(file, mode="r") as potfile:
        assert potfile.read().strip() == template


def test_duplicate_keys(file, keys):
    keys_with_duplicates = list(keys)
    keys_with_duplicates.append(keys.pop())

    with POTFile(file, "w") as potfile:
        with pytest.raises(KeyError):
            for key in keys_with_duplicates:
                potfile.write(key=key, check_key=True)


def test_comment_adding(file):
    comment = "test_comment"
    with POTFile(file, "w") as potfile:
        potfile.write(key="test", comment=comment)

    with open(file, mode="r") as potfile:
        assert len(re.findall(r"#\s+" + comment, potfile.read())) == 1


def test_passing_file_object(create_potfile, file, keys):
    with open(file, mode="r", encoding="utf-8") as potfile:
        with POTFile(potfile) as f:
            assert keys == set(f.keys)


def test_passing_invalid_file():
    with pytest.raises(TypeError):
        POTFile(object, mode="r")


def test_close_method(create_potfile, file, keys):
    with open(file, mode="r", encoding="utf-8") as f:
        potfile = POTFile(f)
        potfile.close()
        assert f.closed
