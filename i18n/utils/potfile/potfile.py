from .types import (
    TextFileMode
)
from .constants import (
    TEMPLATES,
    MSGID_REGEX
)


class POTFile:
    def __init__(self, file: str, mode: TextFileMode, template: str | None = None):
        self._path = file
        self._mode = mode
        self._template = template
        self._file = open(self._path, mode=mode)
        self._cached_keys = set()

        if self._mode == 'w':
            self._write_template()

        if self._mode in {'a', 'r'}:
            self._load_keys()

    def _write_template(self):
        if self._template:
            self._file.write(self._template)

    def _load_keys(self):
        for line in self._file:
            if MSGID_REGEX.match(line):
                result = MSGID_REGEX.findall(line)[0]
                self._cached_keys.add(result)

    def write(self, key: str, comment: str = None, check_key: bool = True):
        if check_key and key in self._cached_keys:
            raise KeyError(f'Duplicate key: {key}')

        self._cached_keys.add(key)
        self._file.write(f'# {comment}\nmsgid "{key}"\nmsgstr ""\n')

    @property
    def keys(self):
        yield from self

    def close(self):
        self._file.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self._file.close()

    def __iter__(self):
        yield from self._cached_keys
