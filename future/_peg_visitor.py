from typing import Any, Protocol, Set

from arpeggio import NonTerminal, PTNodeVisitor, Terminal

from ._types import Keyword, Regex, Rule, Text


class SupportsChildren(Protocol):
    ...


class ModuleVisitor(PTNodeVisitor):
    class_name: str
    keywords: Set[Keyword]

    def __init__(self, class_name: str, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.class_name = class_name
        self.keywords = set()

    def visit_KEYWORD(self, node: Terminal, _: SupportsChildren) -> Keyword:
        keyword = Keyword(node.value[1:-1])
        self.keywords.add(keyword)
        return keyword

    def visit_REGEX(self, node: NonTerminal, _: SupportsChildren) -> Regex:
        (terminal,) = node
        assert isinstance(terminal, Terminal)
        return Regex(terminal.value[2:-1])

    def visit_TEXT(self, node: NonTerminal, _: SupportsChildren) -> Text:
        (terminal,) = node
        assert isinstance(terminal, Terminal)
        return Text(terminal.value[1:-1])

    def __visit_RULE(self, node: Terminal, _: SupportsChildren) -> Rule:
        return Rule(node.value.replace("-", "_"))

    visit_LEXICAL_RULE = __visit_RULE
    visit_SYNTAX_RULE = __visit_RULE
