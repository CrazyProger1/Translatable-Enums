import argparse

from i18n.settings import (
    APP,
    DESCRIPTION
)


def setup_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog=APP,
        description=DESCRIPTION
    )

    parser.add_argument(
        'source',
        default='main.py',
        help='The source file to extract translations from (main file of application)',
        nargs='?'
    )

    parser.add_argument(
        'destination',
        default='main.pot',
        help='Destination .pot file',
        nargs='?'
    )

    parser.add_argument(
        '-v', '--version',
        action='store_true',
        help='show version and exit',
        default=False
    )

    return parser


def main():
    parser = setup_argparse()
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()
