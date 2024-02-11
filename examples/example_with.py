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

with language('uk_UA'):
    print(Messages.HELLO, Messages.WORLD)  # Привіт, Світ!

print(Messages.HELLO, Messages.WORLD)  # Hello, World!
