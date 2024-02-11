import pytest

from i18n.utils.clsutils import (
    iter_subclasses
)


class FirstClass:
    pass


class FirstSubclass(FirstClass):
    pass


class FirstSubSubClass(FirstSubclass):
    pass


def test_iter_subclasses_max_level_1():
    subclasses = tuple(iter_subclasses(FirstClass, max_level=1))

    assert len(subclasses) == 1
    assert subclasses[0] == FirstSubclass


def test_iter_subclasses_max_level_neg_1():
    subclasses = tuple(iter_subclasses(FirstClass, max_level=-1))

    assert len(subclasses) == 2


def test_iter_subclasses_max_level_0():
    subclasses = tuple(iter_subclasses(FirstClass, max_level=0))

    assert len(subclasses) == 0
