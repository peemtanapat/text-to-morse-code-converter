import re

regex_pattern = r'([A-Za-z0-9\/\?\.\,\-\(\)\s]*)'
pattern = re.compile(regex_pattern)


def check_pattern(text: str) -> bool:
    print(text)
    result: bool = bool(pattern.fullmatch(text))
    return result
