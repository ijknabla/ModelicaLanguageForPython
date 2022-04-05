from arpeggio import EOF, RegExMatch
from typing import Any


# grammar rules
def grammar() -> Any:
    return (EOF,)


# comment rule
def comment() -> Any:
    return [
        RegExMatch(r"//.*"),
        RegExMatch(r"/\*([^*]|\*[^/])*\*/"),
    ]
