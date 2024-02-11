# Translatable-Enums

<p align="center">
<img src="docs/logo.png" alt="Lib logo">
</p>

<p align="center">
<a href="https://github.com/CrazyProger1/RestyClient/blob/master/LICENSE"><img alt="GitHub" src="https://img.shields.io/github/license/CrazyProger1/RestyClient"></a>
<a href="https://github.com/CrazyProger1/RestyClient/releases/latest"><img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/CrazyProger1/RestyClient"></a>
<a href="https://pypi.org/project/resty-client/"><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/resty-client"></a>
<img src="https://img.shields.io/badge/coverage-97%25-brightgreen" alt="Coverage"/>
</p>

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
from i18n import TranslatableEnum, set_language


class Messages(TranslatableEnum):
    HELLO = 'Hello,'
    WORLD = 'World!'


print(Messages.HELLO, Messages.WORLD)  # Hello, World!

set_language('ua')

print(Messages.HELLO, Messages.WORLD)  # Привіт, Світ!
```

## Status

``0.0.1`` - RELEASED

## Licence

Translatable-Enums is released under the MIT License. See the bundled [LICENSE](LICENSE) file for details.