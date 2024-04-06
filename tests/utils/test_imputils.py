import pytest

from i18n.utils.imputils import import_module


@pytest.fixture
def module_file():
    return "tests/utils/module.py"


@pytest.fixture
def module_dir():
    return "tests/utils/module"


def test_import_module(module_file):
    module = import_module(module_file)

    assert hasattr(module, "MyClass")


def test_import_folder_module(module_dir):
    module = import_module(module_dir)

    assert hasattr(module, "MyClass")


def test_import_error():
    with pytest.raises(ImportError):
        import_module("QQQQ")
