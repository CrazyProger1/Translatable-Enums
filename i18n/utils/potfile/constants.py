import re

TEMPLATES = {
    "common": """
msgid ""
msgstr ""
"Project-Id-Version: \\n"
"POT-Creation-Date: \\n"
"Last-Translator: \\n"
"Language-Team: \\n"
"Language: \\n"
"MIME-Version: \\n"
"Content-Type: text/plain; charset=utf-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"Key-Format: {key_format}\\n"

"""
}

MSGID_REGEX = re.compile(r"^msgid\s+\"(.+?)\"\s*")
HEADER_REGEXES = {
    "Key-Format": re.compile(r"^\"Key-Format:.+\""),
}
