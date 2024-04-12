# Translatable-Enums Changelog

## v0.0.1:

- Added base functionality (Translatable Enums)
- Added translation-keys extract functionality

## v0.0.2

- Added one-field translation (field.language)

## v0.0.3

- Expanded supported range of Python versions(3.10+)
- Added more tests. Improved coverage percentage (to 99%)

## v0.0.4

- Fixed assertion error occurred when context firstly used

## v0.0.5

- Added comments:

```
# Messages.WORLD
msgid "World!"
msgstr ""
```

- Added more tests. Improved coverage percentage (to 100%)

## v0.0.6

- Added key-format:


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
