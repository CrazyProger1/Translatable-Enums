from i18n import TranslatableEnum, extract_keys


class MyEnum(TranslatableEnum):
    HELLO = 'hello,'
    WORLD = 'world'


print(MyEnum.HELLO, MyEnum.WORLD)
