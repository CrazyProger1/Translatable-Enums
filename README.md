# Translatable-Enums

<p align="center">
<img src="https://github.com/CrazyProger1/Translatable-Enums/blob/master/resources/images/logo.png" alt="Lib logo">
</p>

<p align="center">
<a href="https://github.com/CrazyProger1/Translatable-Enums/blob/master/LICENSE"><img alt="GitHub" src="https://img.shields.io/github/license/CrazyProger1/Translatable-Enums"></a>
<a href="https://github.com/CrazyProger1/Translatable-Enums/releases/latest"><img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/CrazyProger1/Translatable-Enums"></a>
<a href="https://pypi.org/project/translatable-enums/"><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/translatable-enums"></a>
<img src="https://img.shields.io/badge/coverage-100%25-brightgreen" alt="Coverage"/>
<a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code Style"></a>
</p>

Translatable-Enums is an i18n tool which uses built-in Enums as a convenient way to store translation keys.

## Key-Features

- No dependencies except the Python's standard library. Based on built-in enums & gettext
- Powerful utility for extracting translation-keys
- Easy-to-Use

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
    set_language,
    language
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

print(Messages.HELLO.language('uk'), Messages.WORLD.language('en'))  # Привіт, World!

with language('uk_UA'):
    print(Messages.HELLO, Messages.WORLD)  # Привіт, Світ!

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

# Messages.WORLD
msgid "World!"
msgstr ""

# Messages.HELLO
msgid "Hello,"
msgstr ""
```

#### Key-Format

```shell
python -m i18n main.py application.pot --key-format "{enum}.{name}.{value}"
```

Default: ```"{value}"```

- enum - enum name
- name - attribute name
- value - attribute value

Examples:

```{enum}.{name}.{value}```
```
# Messages.WORLD
msgid "Messages.WORLD.World!"
msgstr ""
```

```{enum}.{name}```
```
# Messages.WORLD
msgid "Messages.WORLD"
msgstr ""
```


```{value}```
```
# Messages.WORLD
msgid "World!"
msgstr ""
```


### Examples

See [/examples](examples/) for more examples.

## Status

```0.0.6``` - **RELEASED**

## Licence

Translatable-Enums is released under the MIT License. See the
bundled [LICENSE](https://github.com/CrazyProger1/Translatable-Enums/blob/master/LICENSE) file for details.