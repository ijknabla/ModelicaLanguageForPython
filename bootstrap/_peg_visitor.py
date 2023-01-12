from ast import AnnAssign, Constant, Ellipsis, Module
from typing import Any, Iterable, Set

from arpeggio import NonTerminal, PTNodeVisitor, Terminal
from typing_extensions import Protocol

from ._ast_generator import (
    create_ann_assign,
    create_attribute,
    create_module_with_class,
    create_subscript,
    create_tuple,
)
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

    def visit_grammar(
        self, _: PTNodeVisitor, children: SupportsChildren
    ) -> Module:
        sorted_keywords = sorted(self.keywords)

        return create_module_with_class(
            imports=[],
            import_froms=[
                ("typing", ["ClassVar", "Tuple"]),
            ],
            class_name=self.class_name,
            class_bases=[],
            class_body=[
                self.__create_keywords_classvar(sorted_keywords),
            ],
        )

    @staticmethod
    def __create_keywords_classvar(keywords: Iterable[Keyword]) -> AnnAssign:
        return create_ann_assign(
            target="_keywords_",
            annotation=create_subscript(
                value=create_attribute("ClassVar"),
                slice=create_subscript(
                    value=create_attribute("Tuple"),
                    slice=create_tuple(
                        elts=[create_attribute("str"), Ellipsis()]
                    ),
                ),
            ),
            value=create_tuple(
                elts=[Constant(value=keyword) for keyword in sorted(keywords)]
            ),
        )
