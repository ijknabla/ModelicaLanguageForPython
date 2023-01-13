from ast import AnnAssign, Ellipsis, FunctionDef, Module, Tuple, expr
from typing import (
    Any,
    Callable,
    DefaultDict,
    Dict,
    Iterator,
    Sequence,
    Set,
    Union,
)

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
    create_constant,
    create_function_def,
    create_list,
    create_module_with_class,
    create_subscript,
    create_tuple,
    pattern2regex,
    regex2pattern,
    resolve_pattern,
    text2pattern,
)
from ._types import Keyword, Regex, Rule, Text


class SupportsChildren(Protocol):
    KEYWORD: Sequence[Keyword]
    LEXICAL_REFERENCE: Sequence[Rule]
    LEXICAL_RULE: Sequence[Rule]
    REGEX: Sequence[Regex]
    SYNTAX_REFERENCE: Sequence[Rule]
    SYNTAX_RULE: Sequence[Rule]
    TEXT: Sequence[Text]
    lexical_expression: Sequence[Pattern]
    lexical_ordered_choice: Sequence[Pattern]
    lexical_primary: Sequence[Pattern]
    lexical_quantity: Sequence[Pattern]
    lexical_sequence: Sequence[Pattern]
    syntax_expression: Sequence[expr]
    syntax_ordered_choice: Sequence[expr]
    syntax_primary: Sequence[expr]
    syntax_quantity: Sequence[expr]
    syntax_sequence: Sequence[expr]


class ModuleVisitor(PTNodeVisitor):
    class_name: str
    keywords: Set[Keyword]
    pattern_references: DefaultDict[Rule, PatternReference]
    rule_definitions: Dict[Rule, Callable[[], FunctionDef]]
    source: str

    def __init__(
        self, class_name: str, source: str, *args: Any, **kwargs: Any
    ) -> None:
        super().__init__(*args, **kwargs)
        self.class_name = class_name
        self.keywords = set()
        self.pattern_references = DefaultDict[Rule, PatternReference](
            PatternReference
        )
        self.rule_definitions = {}
        self.source = source

    def visit_grammar(
        self, _: PTNodeVisitor, children: SupportsChildren
    ) -> Module:
        return create_module_with_class(
            imports=[],
            import_froms=[
                ("typing", ["ClassVar", "Tuple"]),
                ("arpeggio", ["Optional", "RegExMatch", "ZeroOrMore"]),
                (
                    "modelica_language._backend",
                    [
                        "ParsingExpressionLike",
                        "not_start_with_keyword",
                        "returns_parsing_expression",
                    ],
                ),
            ],
            class_name=self.class_name,
            class_bases=[],
            class_body=[
                *self.__keyword_definitions(),
                *map(lambda f: f(), self.rule_definitions.values()),
            ],
        )

    def __keyword_definitions(self) -> Iterator[Union[AnnAssign, FunctionDef]]:
        sorted_keywords = sorted(self.keywords)
        yield create_ann_assign(
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
                elts=[
                    create_constant(value=keyword)
                    for keyword in sorted_keywords
                ]
            ),
        )
        for keyword in sorted_keywords:
            name = keyword.upper()
            regex = Regex(rf"{keyword}(?![0-9A-Z_a-z])")

            yield create_function_def(
                name=name,
                args=[],
                value=create_call(
                    "RegExMatch",
                    args=[create_constant(value=regex)],
                ),
                decorator_list=["staticmethod", "returns_parsing_expression"],
                returns="RegExMatch",
            )

    def visit_lexical_rule_statement(
        self, _: ParseTreeNode, children: SupportsChildren
    ) -> None:
        (name,) = children.LEXICAL_RULE
        (pattern,) = children.lexical_expression

        self.pattern_references[name].target = pattern
        if name == "IDENT":
            decorator_list = [
                "classmethod",
                "not_start_with_keyword",
                "returns_parsing_expression",
            ]
            args = ["cls"]
        else:
            decorator_list = [
                "staticmethod",
                "returns_parsing_expression",
            ]
            args = []

        def rule_definition() -> FunctionDef:
            value = pattern2regex(resolve_pattern(pattern))

            return create_function_def(
                name=name,
                args=args,
                value=create_call(
                    "RegExMatch",
                    args=[create_constant(value=value)],
                ),
                decorator_list=decorator_list,
                returns="RegExMatch",
            )

        self.rule_definitions[name] = rule_definition

    def visit_syntax_rule_statement(
        self, _: ParseTreeNode, children: SupportsChildren
    ) -> None:
        (name,) = children.SYNTAX_RULE
        (value,) = children.syntax_expression

        def rule_definition() -> FunctionDef:
            return create_function_def(
                name=name,
                args=["cls"],
                value=value,
                decorator_list=["classmethod", "returns_parsing_expression"],
                returns="ParsingExpressionLike",
            )

        self.rule_definitions[name] = rule_definition

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

    def visit_syntax_primary(
        self, _: ParseTreeNode, children: SupportsChildren
    ) -> expr:
        if children.syntax_expression:
            (expression,) = children.syntax_expression
            return expression
        elif children.KEYWORD:
            (keyword,) = children.KEYWORD
            return create_attribute(f"cls.{keyword.upper()}")
        elif children.TEXT:
            (text,) = children.TEXT
            return create_constant(value=text)
        elif children.SYNTAX_REFERENCE:
            (rule,) = children.SYNTAX_REFERENCE
            return create_attribute(f"cls.{rule}")
        raise NotImplementedError()

    def visit_syntax_quantity(
        self, node: NonTerminal, children: SupportsChildren
    ) -> expr:
        if children.syntax_expression:
            head, *tail = children.syntax_expression
            if not tail and isinstance(head, Tuple):
                args = head.elts
            else:
                args = [head, *tail]

            L, _, R = node
            assert isinstance(L, Terminal)
            assert isinstance(R, Terminal)
            if L == "[" and R == "]":
                return create_call(
                    func="Optional",
                    args=args,
                )
            elif L == "{" and R == "}":
                return create_call(
                    func="ZeroOrMore",
                    args=args,
                )
        elif children.syntax_primary:
            (primary,) = children.syntax_primary
            return primary
        raise NotImplementedError()

    def visit_syntax_sequence(
        self, _: ParseTreeNode, children: SupportsChildren
    ) -> expr:
        head, *tail = children.syntax_quantity
        if tail:
            return create_tuple(elts=[head, *tail])
        else:
            return head

    def visit_syntax_ordered_choice(
        self, _: ParseTreeNode, children: SupportsChildren
    ) -> expr:
        head, *tail = children.syntax_sequence
        if tail:
            return create_list(elts=[head, *tail])
        else:
            return head

    def visit_syntax_expression(
        self, _: ParseTreeNode, children: SupportsChildren
    ) -> expr:
        (child,) = children.syntax_ordered_choice
        return child

    def __get_source(self, node: ParseTreeNode) -> str:
        begin = node.position
        end = node.position_end
        return self.source[begin:end]
