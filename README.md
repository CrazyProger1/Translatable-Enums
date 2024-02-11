# Translatable-Enums

<p align="center">
<img src="resources/images/logo.png" alt="Lib logo">
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

To extract the translation-keys from file:

```shell
python -m i18n main.py application.pot
```

For more examples, see the [examples](./examples) directory ;)

## Status

``0.0.1`` - RELEASED

## Licence

Translatable-Enums is released under the MIT License. See the bundled [LICENSE](LICENSE) file for details.