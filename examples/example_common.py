from i18n import (
    TranslatableEnum,
    set_domain,
    set_language
)


class Messages(TranslatableEnum):
    HELLO = 'Hello,'
    WORLD = 'World!'


set_domain('app', './resources/languages')
set_language('en')

print(Messages.HELLO, Messages.WORLD)  # Hello, World!

set_language('uk')

print(Messages.HELLO, Messages.WORLD)  # Привіт, Світ!
