import argparse
import sys

from i18n.settings import APP, DESCRIPTION, VERSION
from i18n.tools import extract_keys, save_pot
from i18n.types import BaseTranslatableEnum
from i18n.utils.gettext import set_language
from i18n.utils.imputils import import_module
from i18n.utils.potfile import TEMPLATES


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

    parser.add_argument(
        "-k",
        "--key-format",
        required=False,
        default="{value}",
        help='key format (name - attribute name, value - attribute value, enum - enum name). Default: "{value}"',
    )

    return parser


def show_version():
    print(VERSION)


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
    save_pot(
        file=args.destination,
        keys=keys,
        template=TEMPLATES[args.template],
        key_format=args.key_format,
    )


if __name__ == "__main__":
    main()
