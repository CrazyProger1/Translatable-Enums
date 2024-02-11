# Translatable-Enums

<p align="center">
<img src="https://github.com/CrazyProger1/Translatable-Enums/blob/master/resources/images/logo.png" alt="Lib logo">
</p>

<p align="center">
<a href="https://github.com/CrazyProger1/Translatable-Enums/blob/master/LICENSE"><img alt="GitHub" src="https://img.shields.io/github/license/CrazyProger1/Translatable-Enums"></a>
<a href="https://github.com/CrazyProger1/Translatable-Enums/releases/latest"><img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/CrazyProger1/Translatable-Enums"></a>
<a href="https://pypi.org/project/translatable-enums/"><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/translatable-enums"></a>
<img src="https://img.shields.io/badge/coverage-98%25-brightgreen" alt="Coverage"/>
</p>

Translatable-Enums is an i18n tool which uses built-in Enums as a convenient way to store translation keys.

## Installation

You can use PIP:

```shell
pip install translatable-enums
```

Or Poetry:

```shell
poetry add translatable-enums
```

## Getting-Started

```python
from i18n import (
    TranslatableEnum,
    set_domain,
    set_language
)


class Messages(TranslatableEnum):
    HELLO = 'Hello,'
    WORLD = 'World!'


set_domain('app', './resources/languages')
set_language('en_US')

print(Messages.HELLO, Messages.WORLD)  # Hello, World!

set_language('uk_UA')

print(Messages.HELLO, Messages.WORLD)  # Привіт, Світ!

set_language('fr_FR')

print(Messages.HELLO, Messages.WORLD)  # Bonjour le monde!
```

### Extraction-Tools

To extract the translation-keys from application:

```shell
python -m i18n main.py application.pot
```

You will obtain a [.pot](https://pofile.net/) file like this:

```potfile
msgid ""
msgstr ""
"Project-Id-Version: \n"
"POT-Creation-Date: \n"
"Last-Translator: \n"
"Language-Team: \n"
"Language: \n"
"MIME-Version: \n"
"Content-Type: text/plain; charset=utf-8\n"
"Content-Transfer-Encoding: 8bit\n"

msgid "Hello,"
msgstr ""

msgid "World!"
msgstr ""
```

## Status

``0.0.2`` - RELEASED

## Licence

Translatable-Enums is released under the MIT License. See the bundled [LICENSE](https://github.com/CrazyProger1/Translatable-Enums/blob/master/LICENSE) file for details.