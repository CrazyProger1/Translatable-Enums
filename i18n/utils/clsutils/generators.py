import inspect
from typing import Generator


def iter_subclasses(cls: type, max_level: int = -1) -> Generator:
    assert inspect.isclass(cls)
    assert isinstance(max_level, int)

    if max_level == 0:
        return

    for subcls in cls.__subclasses__():
        yield subcls
        for subsubcls in iter_subclasses(subcls, max_level - 1):
            yield subsubcls
