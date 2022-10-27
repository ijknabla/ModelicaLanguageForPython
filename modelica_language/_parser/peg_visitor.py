import re
from collections import deque
from copy import copy
from dataclasses import dataclass
from typing import (
    Any,
    ClassVar,
    Collection,
    Dict,
    Iterable,
    Iterator,
    List,
    Mapping,
    MutableMapping,
    NewType,
    Optional,
    Set,
    Tuple,
    Type,
    TypeVar,
    Union,
)

import arpeggio
from typing_extensions import Literal, Protocol

from ..exceptions import SemanticError

T_key = TypeVar("T_key")
T_value = TypeVar("T_value")

PEGRuleName = NewType("PEGRuleName", str)
PyRuleName = NewType("PyRuleName", str)
RegExPattern = NewType("RegExPattern", str)


class LexicalElementLike(Protocol):
    @property
    def pattern(self) -> Optional[RegExPattern]:
        ...

    def getParsingExpression(self) -> arpeggio.ParsingExpression:
        ...


SyntaxElementLike = Union[
    arpeggio.ParsingExpression,
    "NonTerminal",
    "LexicalReference",
    "SyntaxReference",
]


class TerminalNode(Protocol):
    value: str


class LexicalChildren(Protocol):
    LEXICAL_ASSIGNMENT: Collection[str]
    LEXICAL_INPLACE_OR: Collection[str]
    NOT: Collection[str]
    OPEN_SQUARE_BRACKET: Collection[str]
    CLOSE_SQUARE_BRACKET: Collection[str]
    OPEN_BRACE: Collection[str]
    CLOSE_BRACE: Collection[str]
    LEXICAL_RULE: Collection[PEGRuleName]
    lexical_expression: Collection[LexicalElementLike]
    lexical_sequence: Collection[LexicalElementLike]
    lexical_quantity: Collection[LexicalElementLike]
    lexical_term: Collection[LexicalElementLike]
    lexical_primary: Collection[LexicalElementLike]


class SyntaxChildren(Protocol):
    SYNTAX_ASSIGNMENT: Collection[str]
    SYNTAX_INPLACE_OR: Collection[str]
    OPEN_SQUARE_BRACKET: Collection[str]
    CLOSE_SQUARE_BRACKET: Collection[str]
    OPEN_BRACE: Collection[str]
    CLOSE_BRACE: Collection[str]
    LEXICAL_RULE: Collection[PEGRuleName]
    SYNTAX_RULE: Collection[PEGRuleName]
    EOF_RULE: Collection[PEGRuleName]
    syntax_expression: Collection[SyntaxElementLike]
    syntax_sequence: Collection[SyntaxElementLike]
    syntax_quantity: Collection[SyntaxElementLike]
    syntax_primary: Collection[SyntaxElementLike]


@dataclass(frozen=True)
class NonTerminal:
    ParsingExpressionType: Type[arpeggio.ParsingExpression]
    nodes: Tuple[SyntaxElementLike, ...]

    def getParsingExpression(self) -> arpeggio.ParsingExpression:
        return self.ParsingExpressionType()


class Reference:
    __ruleName: PEGRuleName

    def __init__(self, ruleName: PEGRuleName):
        self.__ruleName = ruleName

    @property
    def ruleName(self) -> PEGRuleName:
        return self.__ruleName

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.ruleName!r}, ...)"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Reference) and self.ruleName == other.ruleName

    def __hash__(self) -> int:
        return hash(self.ruleName)


class LexicalReference(Reference):
    __target: Optional[LexicalElementLike]

    def __init__(
        self, ruleName: PEGRuleName, target: Optional[LexicalElementLike]
    ):
        super().__init__(ruleName)
        self.__target = target

    @property
    def target(self) -> LexicalElementLike:
        if self.__target is None:
            raise SemanticError(f"{self.ruleName!r} is not defined")
        return self.__target

    @target.setter
    def target(self, target: LexicalElementLike) -> None:
        self.__target = target

    @property
    def pattern(self) -> Optional[RegExPattern]:
        return self.target.pattern

    def getParsingExpression(self) -> arpeggio.ParsingExpression:
        parsingExpression = self.target.getParsingExpression()
        if parsingExpression.root and parsingExpression.rule_name != peg2py(
            self.ruleName
        ):
            parsingExpression = copy(parsingExpression)

        parsingExpression.root = True
        parsingExpression.rule_name = peg2py(self.ruleName)

        return parsingExpression


class SyntaxReference(Reference):
    __target: Optional[SyntaxElementLike]

    def __init__(
        self, ruleName: PEGRuleName, target: Optional[SyntaxElementLike]
    ):
        super().__init__(ruleName)
        self.__target = target

    @property
    def target(self) -> SyntaxElementLike:
        if self.__target is None:
            raise SemanticError(f"{self.ruleName!r} is not defined")
        return self.__target

    @target.setter
    def target(self, target: SyntaxElementLike) -> None:
        self.__target = target


@dataclass(frozen=True)
class Keyword:
    value: str

    @classmethod
    def fromTerminalNode(cls, node: TerminalNode) -> "Keyword":
        return cls(node.value[1:-1])

    @property
    def ruleName(self) -> PEGRuleName:
        return PEGRuleName(f"${self.value}$")

    @property
    def pattern(self) -> RegExPattern:
        return RegExPattern(rf"{self.value}(?![0-9A-Z_a-z])")

    def getParsingExpression(self) -> arpeggio.ParsingExpression:
        regExMatch = arpeggio.RegExMatch(self.pattern)
        regExMatch.compile()
        return regExMatch


@dataclass(frozen=True)
class Text:
    value: str

    @classmethod
    def fromTerminalNode(cls, node: TerminalNode) -> "Text":
        return cls(node.value[1:-1])

    @property
    def pattern(self) -> RegExPattern:
        return RegExPattern(re.escape(self.value))

    def getParsingExpression(self) -> arpeggio.ParsingExpression:
        return arpeggio.StrMatch(self.value)


@dataclass(frozen=True)
class RegEx:
    pattern: RegExPattern

    @classmethod
    def fromTerminalNode(cls, node: TerminalNode) -> "RegEx":
        return cls(RegExPattern(node.value[2:-1]))

    def getParsingExpression(self) -> arpeggio.ParsingExpression:
        regExMatch = arpeggio.RegExMatch(self.pattern)
        regExMatch.compile()
        return regExMatch


@dataclass
class LexicalNot:
    target: LexicalElementLike

    @property
    def pattern(self) -> Optional[RegExPattern]:
        return None

    def getParsingExpression(self) -> arpeggio.ParsingExpression:
        return arpeggio.Not(nodes=[self.target.getParsingExpression()])


@dataclass
class LexicalRepeat:
    target: LexicalElementLike
    max: Union[None, Literal[1]]

    @property
    def pattern(self) -> Optional[RegExPattern]:
        pattern = self.target.pattern
        if pattern is None:
            return None
        elif self.max == 1:
            return RegExPattern(r"({})?".format(pattern))
        elif self.max is None:
            return RegExPattern(r"({})*".format(pattern))
        raise NotImplementedError()

    def getParsingExpression(self) -> arpeggio.ParsingExpression:
        pattern = self.pattern
        if pattern is not None:
            match = arpeggio.RegExMatch(pattern)
            match.compile()
            return match
        elif self.max == 1:
            return arpeggio.Optional(
                nodes=[self.target.getParsingExpression()]
            )
        elif self.max is None:
            return arpeggio.ZeroOrMore(
                nodes=[self.target.getParsingExpression()]
            )


@dataclass
class AbstractLexicalSequence:
    parsingExpressionType: ClassVar[Type[arpeggio.ParsingExpression]]
    targets: Collection[LexicalElementLike]

    def __iter__(self) -> Iterator[LexicalElementLike]:
        yield from self.targets

    @staticmethod
    def combineRegEx(patterns: Iterable[RegExPattern]) -> RegExPattern:
        raise NotImplementedError()

    @property
    def pattern(self) -> Optional[RegExPattern]:
        patterns = self.__patterns
        if patterns is None:
            return None
        return self.combineRegEx(patterns)

    def getParsingExpression(self) -> arpeggio.ParsingExpression:
        def parsingExpressions() -> Iterator[arpeggio.ParsingExpression]:
            patterns: List[RegExPattern] = []
            for target in self.targets:
                if target.pattern is not None:
                    patterns.append(target.pattern)
                    continue

                if patterns:
                    match = arpeggio.RegExMatch(self.combineRegEx(patterns))
                    match.compile()
                    yield match
                    patterns.clear()

                yield target.getParsingExpression()

            if patterns:
                match = arpeggio.RegExMatch(self.combineRegEx(patterns))
                match.compile()
                yield match

        head, *tail = parsingExpressions()
        if not tail:
            return head
        else:
            return self.parsingExpressionType(nodes=(head, *tail))

    @property
    def __patterns(self) -> Optional[List[RegExPattern]]:
        result: List[RegExPattern] = []
        for pattern in (item.pattern for item in self):
            if pattern is not None:
                result.append(pattern)
            else:
                return None
        return result

    @classmethod
    def fromElements(
        cls,
        elements: Iterable[LexicalElementLike],
    ) -> LexicalElementLike:
        head, *tail = cls.__flatten(elements)
        if not tail:
            return head
        else:
            return cls([head, *tail])

    @classmethod
    def __flatten(
        cls, elements: Iterable[LexicalElementLike]
    ) -> Iterator[LexicalElementLike]:
        for element in elements:
            if isinstance(element, cls):
                yield from cls.__flatten(element)
            else:
                yield element


class LexicalSequence(AbstractLexicalSequence):
    parsingExpressionType: ClassVar[
        Type[arpeggio.ParsingExpression]
    ] = arpeggio.Sequence

    @staticmethod
    def combineRegEx(patterns: Iterable[RegExPattern]) -> RegExPattern:
        return RegExPattern(rf"({''.join(patterns)})")


class LexicalOrderedChoice(AbstractLexicalSequence):
    parsingExpressionType: ClassVar[
        Type[arpeggio.ParsingExpression]
    ] = arpeggio.OrderedChoice

    @staticmethod
    def combineRegEx(patterns: Iterable[RegExPattern]) -> RegExPattern:
        return RegExPattern(rf"({'|'.join(patterns)})")


def peg2py(ruleName: PEGRuleName) -> PyRuleName:
    return PyRuleName(re.sub(r"[$-]", "_", ruleName))


class PEGVisitor(arpeggio.PTNodeVisitor):
    __rootRuleName: PEGRuleName
    __comentRuleName: Optional[PEGRuleName]

    __references: MutableMapping[
        PEGRuleName, Union[LexicalReference, SyntaxReference]
    ]

    def __init__(
        self,
        rootRuleName: PEGRuleName,
        commentRuleName: Optional[PEGRuleName],
        *args: Any,
        **kwargs: Any,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.__rootRuleName = rootRuleName
        self.__comentRuleName = commentRuleName
        self.__references = {}

    def __visit_symbol(self, node: TerminalNode, _: Any) -> str:
        return node.value

    visit_NOT = __visit_symbol
    visit_OPEN_SQUARE_BRACKET = __visit_symbol
    visit_CLOSE_SQUARE_BRACKET = __visit_symbol
    visit_OPEN_BRACE = __visit_symbol
    visit_CLOSE_BRACE = __visit_symbol
    visit_LEXICAL_ASSIGNMENT = __visit_symbol
    visit_LEXICAL_INPLACE_OR = __visit_symbol

    def visit_LEXICAL_KEYWORD(
        self, node: TerminalNode, _: Any
    ) -> LexicalElementLike:
        return Keyword.fromTerminalNode(node)

    def visit_LEXICAL_TEXT(
        self, node: TerminalNode, _: Any
    ) -> LexicalElementLike:
        return Text.fromTerminalNode(node)

    def visit_LEXICAL_REGEX(
        self, node: TerminalNode, _: Any
    ) -> LexicalElementLike:
        return RegEx.fromTerminalNode(node)

    def visit_lexical_reference(
        self, _: Any, children: LexicalChildren
    ) -> LexicalElementLike:
        (ruleName,) = children.LEXICAL_RULE
        return self.__getLexicalReference(ruleName)

    def visit_lexical_term(
        self, _: Any, children: LexicalChildren
    ) -> LexicalElementLike:
        (primary,) = children.lexical_primary
        if children.NOT:
            return LexicalNot(primary)
        else:
            return primary

    def visit_lexical_quantity(
        self, _: Any, children: LexicalChildren
    ) -> LexicalElementLike:
        if children.OPEN_SQUARE_BRACKET and children.CLOSE_SQUARE_BRACKET:
            (expression,) = children.lexical_expression
            return LexicalRepeat(expression, max=1)
        elif children.OPEN_BRACE and children.CLOSE_BRACE:
            (expression,) = children.lexical_expression
            return LexicalRepeat(expression, max=None)
        else:
            (term,) = children.lexical_term
            return term

    def visit_lexical_sequence(
        self, _: Any, children: LexicalChildren
    ) -> LexicalElementLike:
        return LexicalSequence.fromElements(children.lexical_quantity)

    def visit_lexical_ordered_choice(
        self, _: Any, children: LexicalChildren
    ) -> LexicalElementLike:
        return LexicalOrderedChoice.fromElements(children.lexical_sequence)

    def visit_SYNTAX_KEYWORD(
        self, node: TerminalNode, _: Any
    ) -> SyntaxElementLike:
        keyword = Keyword.fromTerminalNode(node)
        parsingExpression = keyword.getParsingExpression()
        parsingExpression.root = True
        parsingExpression.rule_name = peg2py(keyword.ruleName)
        return self.__getSyntaxReference(keyword.ruleName, parsingExpression)

    def visit_SYNTAX_TEXT(
        self, node: TerminalNode, _: Any
    ) -> SyntaxElementLike:
        return Text.fromTerminalNode(node).getParsingExpression()

    def visit_syntax_reference(
        self, _: Any, children: SyntaxChildren
    ) -> SyntaxElementLike:
        if children.LEXICAL_RULE:
            (ruleName,) = children.LEXICAL_RULE
            return self.__getLexicalReference(ruleName)
        elif children.SYNTAX_RULE:
            (ruleName,) = children.SYNTAX_RULE
            return self.__getSyntaxReference(ruleName)
        elif children.EOF_RULE:
            ruleName = PEGRuleName("$EOF$")
            eof = arpeggio.EndOfFile()
            eof.root = True
            eof.rule_name = peg2py(ruleName)
            return self.__getSyntaxReference(ruleName, eof)

        raise NotImplementedError()

    def visit_syntax_quantity(
        self, _: Any, children: SyntaxChildren
    ) -> SyntaxElementLike:
        if children.OPEN_SQUARE_BRACKET and children.CLOSE_SQUARE_BRACKET:
            (expression,) = children.syntax_expression
            return NonTerminal(arpeggio.Optional, nodes=(expression,))
        elif children.OPEN_BRACE and children.CLOSE_BRACE:
            (expression,) = children.syntax_expression
            return NonTerminal(arpeggio.ZeroOrMore, nodes=(expression,))
        else:
            (term,) = children.syntax_primary
            return term

    def visit_syntax_sequence(
        self, _: Any, children: SyntaxChildren
    ) -> SyntaxElementLike:
        head, *tail = children.syntax_quantity
        if not tail:
            return head
        else:
            return NonTerminal(arpeggio.Sequence, nodes=(head, *tail))

    def visit_syntax_ordered_choice(
        self, _: Any, children: SyntaxChildren
    ) -> SyntaxElementLike:
        head, *tail = children.syntax_sequence
        if not tail:
            return head
        else:
            return NonTerminal(arpeggio.OrderedChoice, nodes=(head, *tail))

    def visit_lexical_rule_statement(
        self, _: Any, children: LexicalChildren
    ) -> None:
        (ruleName,) = children.LEXICAL_RULE
        (expression,) = children.lexical_expression
        reference = self.__getLexicalReference(ruleName)
        if children.LEXICAL_ASSIGNMENT:
            reference.target = expression
        elif children.LEXICAL_INPLACE_OR:
            reference.target = LexicalOrderedChoice.fromElements(
                [reference.target, expression]
            )
        else:
            raise NotImplementedError()

    def visit_syntax_rule_statement(
        self, _: Any, children: SyntaxChildren
    ) -> None:
        (ruleName,) = children.SYNTAX_RULE
        (expression,) = children.syntax_expression
        reference = self.__getSyntaxReference(ruleName)
        if children.SYNTAX_ASSIGNMENT:
            reference.target = expression
        elif children.SYNTAX_INPLACE_OR:
            reference.target = NonTerminal(
                arpeggio.OrderedChoice,
                nodes=(reference.target, expression),
            )
        else:
            raise NotImplementedError()

    def visit_grammar(
        self, *_: Any
    ) -> Tuple[
        arpeggio.ParsingExpression, Optional[arpeggio.ParsingExpression]
    ]:
        nonTerminals: Set[NonTerminal] = set()
        lexicalReferences: Set[LexicalReference] = set()
        syntaxReferences: Set[SyntaxReference] = set()

        rootRule = self.__references[self.__rootRuleName]
        PEGVisitor.__resolveDependencies(
            rootRule, nonTerminals, lexicalReferences, syntaxReferences
        )

        commentRule = self.__get(self.__references, self.__comentRuleName)
        if commentRule is not None:
            PEGVisitor.__resolveDependencies(
                commentRule, nonTerminals, lexicalReferences, syntaxReferences
            )

        parsingExpressions: Dict[
            SyntaxElementLike, arpeggio.ParsingExpression
        ] = {}

        for element in lexicalReferences | nonTerminals:
            parsingExpressions[element] = element.getParsingExpression()

        notResolvedReferences = deque(syntaxReferences)
        while notResolvedReferences:
            reference = notResolvedReferences.popleft()
            resolved: arpeggio.ParsingExpression
            if not isinstance(reference.target, arpeggio.ParsingExpression):
                if reference.target not in parsingExpressions:
                    notResolvedReferences.append(reference)
                    continue
                else:
                    resolved = parsingExpressions[reference.target]
            else:
                resolved = reference.target

            if resolved.root and resolved.rule_name != peg2py(
                reference.ruleName
            ):
                resolved = copy(resolved)

            resolved.root = True
            resolved.rule_name = peg2py(reference.ruleName)

            parsingExpressions[reference] = resolved

        for nonTerminal in nonTerminals:
            root = parsingExpressions[nonTerminal]
            for node in nonTerminal.nodes:
                if isinstance(node, arpeggio.ParsingExpression):
                    child = node
                else:
                    child = parsingExpressions[node]
                root.nodes.append(child)

        return (
            parsingExpressions[rootRule],
            self.__get(parsingExpressions, commentRule),
        )

    @staticmethod
    def __get(
        mapping: Mapping[T_key, T_value], key: Optional[T_key]
    ) -> Optional[T_value]:
        return mapping[key] if key is not None else None

    @staticmethod
    def __resolveDependencies(
        element: SyntaxElementLike,
        nonTerminals: Set[NonTerminal],
        lexicalReferences: Set[LexicalReference],
        syntaxReferences: Set[SyntaxReference],
    ) -> None:
        if (
            element in nonTerminals
            or element in lexicalReferences
            or element in syntaxReferences
        ):
            return

        candidates: Set[SyntaxElementLike] = set()
        if isinstance(element, NonTerminal):
            nonTerminals.add(element)
            candidates.update(element.nodes)
        elif isinstance(element, LexicalReference):
            lexicalReferences.add(element)
        elif isinstance(element, SyntaxReference):
            syntaxReferences.add(element)
            candidates.add(element.target)

        for candidate in candidates:

            PEGVisitor.__resolveDependencies(
                candidate,
                nonTerminals,
                lexicalReferences,
                syntaxReferences,
            )

    def __getLexicalReference(
        self,
        ruleName: PEGRuleName,
        target: Optional[LexicalElementLike] = None,
    ) -> LexicalReference:
        if ruleName not in self.__references:
            self.__references[ruleName] = LexicalReference(ruleName, target)
        reference = self.__references[ruleName]
        assert isinstance(reference, LexicalReference)
        return reference

    def __getSyntaxReference(
        self, ruleName: PEGRuleName, target: Optional[SyntaxElementLike] = None
    ) -> SyntaxReference:
        if ruleName not in self.__references:
            self.__references[ruleName] = SyntaxReference(ruleName, target)
        reference = self.__references[ruleName]
        assert isinstance(reference, SyntaxReference)
        return reference


def visit_parse_tree(
    parseTree: arpeggio.ParseTreeNode,
    rootRuleName: str,
    commentRuleName: Optional[str],
    debug: bool,
) -> Tuple[arpeggio.ParsingExpression, Optional[arpeggio.ParsingExpression]]:
    return arpeggio.visit_parse_tree(  # type: ignore
        parseTree,
        PEGVisitor(
            PEGRuleName(rootRuleName),
            PEGRuleName(commentRuleName)
            if commentRuleName is not None
            else None,
            debug=debug,
        ),
    )
