import argparse
import sys
from typing import Iterable

from i18n.settings import APP, DESCRIPTION, VERSION
from i18n.types import BaseTranslatableEnum, Key
from i18n.tools import extract_keys
from i18n.utils.gettext import set_language
from i18n.utils.potfile import POTFile, TEMPLATES
from i18n.utils.imputils import import_module


def setup_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog=APP, description=DESCRIPTION)

    parser.add_argument(
        "source",
        default="main.py",
        help="source file to extract translations from (main file of application)",
        nargs="?",
    )

    parser.add_argument(
        "destination", default="main.pot", help="destination .pot file", nargs="?"
    )

    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="show version and exit",
        default=False,
    )

    parser.add_argument(
        "-t",
        "--template",
        required=False,
        default="common",
        help=".pot file template",
        choices=set(TEMPLATES.keys()),
    )

    return parser


def show_version():
    print(VERSION)


def save_pot(file: str, keys: Iterable[Key], template: str = None) -> None:
    with POTFile(file=file, mode="w", template=template) as potfile:
        for key in keys:
            potfile.write(key=key.key, comment=key.comment)


def main():
    parser = setup_argparse()
    args = parser.parse_args()

    if args.version:
        show_version()
        sys.exit(0)

    source = args.source
    try:
        import_module(source)
    except ImportError:
        raise

    set_language("en")

    keys = extract_keys(base_enum=BaseTranslatableEnum)
    save_pot(file=args.destination, keys=keys, template=TEMPLATES[args.template])


if __name__ == "__main__":
    main()
