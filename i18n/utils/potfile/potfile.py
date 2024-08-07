from io import TextIOWrapper
from typing import TextIO

from .constants import HEADER_REGEXES, MSGID_REGEX
from .types import TextFileMode


class POTFile:
    def __init__(
        self,
        file: str | TextIO,
        mode: TextFileMode = "r",
        template: str | None = None,
        encoding: str | None = None,
    ):
        self._mode = mode
        self._encoding = encoding
        self._template = template
        self._headers = {}
        self._file: TextIO = self._open_file(file)
        self._cached_keys = set()

        if self._mode == "w":
            self._write_template()

        if self._mode in {"a", "r"}:
            self._parse_file()

    def _open_file(self, file_or_path: str | TextIO) -> TextIO:
        if isinstance(file_or_path, str):
            return open(file_or_path, encoding=self._encoding, mode=self._mode)
        elif isinstance(file_or_path, TextIO | TextIOWrapper):
            return file_or_path
        raise TypeError(f"Unsupported type of file parameter: {file_or_path}")

    def _write_template(self):
        if self._template:
            self._file.write(self._template)

    def _parse_file(self):
        for line in self._file:
            for header, regex in HEADER_REGEXES.items():
                result = regex.findall(line)
                if result:
                    self._headers[header] = (
                        result[0]
                        .replace('"', "")
                        .lstrip()
                        .removeprefix(header + ":")
                        .strip()
                        .replace("\\n", "")
                    )

            if MSGID_REGEX.match(line):
                result = MSGID_REGEX.findall(line)[0]
                self._cached_keys.add(result)

    def write(self, key: str, comment: str = None, check_key: bool = True):
        if check_key and key in self._cached_keys:
            raise KeyError(f"Duplicate key: {key}")

        self._cached_keys.add(key)
        text = f'msgid "{key}"\nmsgstr ""\n\n'
        if comment:
            text = f"# {comment}\n{text}"
        self._file.write(text)

    @property
    def keys(self):
        yield from self

    @property
    def headers(self) -> dict[str, str]:
        return self._headers

    def close(self):
        self._file.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self._file.close()

    def __iter__(self):
        yield from self._cached_keys
