from i18n import TranslatableEnum


class MyEnum(TranslatableEnum):
    HELLO = 'hello,'
    WORLD = 'world'


print(MyEnum.HELLO, MyEnum.WORLD)
