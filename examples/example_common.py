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

print(Messages.HELLO.language('uk'), Messages.WORLD.language('en'))  # Привіт, World!
