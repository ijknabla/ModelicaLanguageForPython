from ast import AnnAssign, Constant, Ellipsis, FunctionDef, Module
from typing import Any, DefaultDict, Iterable, Iterator, List, Sequence, Set

from arpeggio import NonTerminal, ParseTreeNode, PTNodeVisitor, Terminal
from typing_extensions import Protocol

from ._ast_generator import (
    OptionalPattern,
    OrderedChoicePattern,
    Pattern,
    PatternReference,
    SequencePattern,
    ZeroOrMorePattern,
    create_ann_assign,
    create_attribute,
    create_call,
    create_function_def,
    create_module_with_class,
    create_subscript,
    create_tuple,
    regex2pattern,
    text2pattern,
)
from ._types import Keyword, Regex, Rule, Text


class SupportsChildren(Protocol):
    LEXICAL_REFERENCE: Sequence[Rule]
    LEXICAL_RULE: Sequence[Rule]
    REGEX: Sequence[Regex]
    TEXT: Sequence[Text]
    lexical_expression: Sequence[Pattern]
    lexical_ordered_choice: Sequence[Pattern]
    lexical_primary: Sequence[Pattern]
    lexical_quantity: Sequence[Pattern]
    lexical_sequence: Sequence[Pattern]


class ModuleVisitor(PTNodeVisitor):
    class_name: str
    keywords: Set[Keyword]
    lexical_rule_order: List[Rule]
    pattern_references: DefaultDict[Rule, PatternReference]

    def __init__(self, class_name: str, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.class_name = class_name
        self.keywords = set()
        self.lexical_rule_order = []
        self.pattern_references = DefaultDict[Rule, PatternReference](
            PatternReference
        )

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

    def visit_lexical_primary(
        self, _: ParseTreeNode, children: SupportsChildren
    ) -> Pattern:
        if children.lexical_expression:
            (expression,) = children.lexical_expression
            return expression
        elif children.REGEX:
            (regex,) = children.REGEX
            return regex2pattern(regex)
        elif children.TEXT:
            (text,) = children.TEXT
            return text2pattern(text)
        elif children.LEXICAL_REFERENCE:
            (rule,) = children.LEXICAL_REFERENCE
            return self.pattern_references[rule]
        raise NotImplementedError()

    def visit_lexical_quantity(
        self, node: NonTerminal, children: SupportsChildren
    ) -> Pattern:
        if children.lexical_expression:
            (child,) = children.lexical_expression
            L, _, R = node
            assert isinstance(L, Terminal)
            assert isinstance(R, Terminal)
            if L == "[" and R == "]":
                return OptionalPattern(child)
            elif L == "{" and R == "}":
                return ZeroOrMorePattern(child)
        elif children.lexical_primary:
            (child,) = children.lexical_primary
            return child
        raise NotImplementedError()

    def visit_lexical_sequence(
        self, _: ParseTreeNode, children: SupportsChildren
    ) -> Pattern:
        return SequencePattern(children.lexical_quantity)

    def visit_lexical_ordered_choice(
        self, _: ParseTreeNode, children: SupportsChildren
    ) -> Pattern:
        return OrderedChoicePattern(children.lexical_sequence)

    def visit_lexical_expression(
        self, _: ParseTreeNode, children: SupportsChildren
    ) -> Pattern:
        (child,) = children.lexical_ordered_choice
        return child

    def visit_lexical_rule_statement(
        self, _: ParseTreeNode, children: SupportsChildren
    ) -> None:
        (rule,) = children.LEXICAL_RULE
        (expression,) = children.lexical_expression
        if rule not in self.lexical_rule_order:
            self.lexical_rule_order.append(rule)
        self.pattern_references[rule].target = expression

    def visit_grammar(
        self, _: PTNodeVisitor, children: SupportsChildren
    ) -> Module:
        sorted_keywords = sorted(self.keywords)

        return create_module_with_class(
            imports=[],
            import_froms=[
                ("typing", ["ClassVar", "Tuple"]),
                ("arpeggio", ["RegExMatch"]),
                ("modelica_language._backend", ["returns_parsing_expression"]),
            ],
            class_name=self.class_name,
            class_bases=[],
            class_body=[
                self.__create_keywords_classvar(sorted_keywords),
                *self.__create_keyword_methods(sorted_keywords),
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

    @staticmethod
    def __create_keyword_methods(
        keywords: Iterable[Keyword],
    ) -> Iterator[FunctionDef]:
        for keyword in keywords:
            name = keyword.upper()
            regex = Regex(rf"{keyword}(?![0-9A-Z_a-z])")

            yield create_function_def(
                name=name,
                args=[],
                value=create_call(
                    "RegExMatch",
                    args=[Constant(value=regex)],
                ),
                decorator_list=["staticmethod", "returns_parsing_expression"],
                returns="RegExMatch",
            )
