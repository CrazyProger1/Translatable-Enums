from i18n import TranslatableEnum, extract_keys
from i18n.utils.gettext import set_language, set_domain

set_language('uk')
set_domain('app', './resources/languages')


class MyEnum(TranslatableEnum):
    HELLO = 'hello,'
    WORLD = 'world'


print(MyEnum.HELLO, MyEnum.WORLD)
