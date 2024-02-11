import pytest

from i18n.utils.potfile import POTFile


@pytest.fixture
def file():
    return 'tests/utils/test.pot'


@pytest.fixture
def keys():
    return {
        'test1',
        'test2',
        'test3'
    }


@pytest.fixture
def create_potfile(file, keys):
    with open(file=file, mode='w') as f:
        for key in keys:
            f.write(f'msgid "{key}"\nmsgstr ""\n')


def test_iter_messages(create_potfile, file, keys):
    with POTFile(file, 'r') as potfile:
        for (message1, message2) in zip(potfile.keys, potfile):
            assert message1 == message2
            keys.remove(message1)

    assert len(keys) == 0


def test_add_keys(file, keys):
    with POTFile(file, 'w') as potfile:
        for key in keys:
            potfile.write(key=key)

    with POTFile(file, 'r') as potfile:
        for message in potfile:
            keys.remove(message)

    assert len(keys) == 0

