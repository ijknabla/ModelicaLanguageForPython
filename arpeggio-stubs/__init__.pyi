from typing import (
    Any,
    Callable,
    Iterable,
    MutableSequence,
    Sequence as _Sequence,
    Union,
)

_AtomicParsingExpressionArgument = Union[
    str,
    CrossRef,
    ParsingExpression,
    Callable[[], ParsingExpression],
]

_ParsingExpressionArgument = Union[
    _AtomicParsingExpressionArgument,
    _Sequence[_AtomicParsingExpressionArgument],
]


class NoMatch(Exception): ...

class DebugPrinter:
    debug: bool
    def __init__(self, *, debug: bool = ...) -> None: ...
    def dprint(
        self,
        message: str,
        indent_change: int = ...,
    ) -> None: ...

class ParsingExpression:
    def __init__(
        self,
        *elements: _ParsingExpressionArgument,
        rule_name: str = ...,
        root: bool = ...,
        nodes: Iterable[_ParsingExpressionArgument] = ...,
        suppress: bool = ...,
    ) -> None: ...
    root: bool
    rule_name: str
    nodes: MutableSequence[Union[CrossRef, ParsingExpression]]
    @property
    def name(self) -> str: ...
    def parse(self, parser: Parser) -> ParseTreeNode: ...

class Sequence(ParsingExpression): ...
class OrderedChoice(Sequence): ...

class Repetition(ParsingExpression):
    """
    eolterm: Any
    sep: Any
    """

    def __init__(
        self,
        *elements: _ParsingExpressionArgument,
        rule_name: str = ...,
        root: bool = ...,
        nodes: Iterable[_ParsingExpressionArgument] = ...,
        suppress: bool = ...,
        sep: _ParsingExpressionArgument = ...,
    ) -> None: ...

class Optional(Repetition): ...
class ZeroOrMore(Repetition): ...
class OneOrMore(Repetition): ...
class SyntaxPredicate(ParsingExpression): ...
class Not(SyntaxPredicate): ...
class Decorator(ParsingExpression): ...
class Combine(Decorator): ...

class Match(ParsingExpression):
    def __init__(
        self,
        rule_name: str,
        root: bool = ...,
    ) -> None: ...

class RegExMatch(Match):
    def __init__(
        self,
        to_match: str,
        rule_name: str = ...,
        root: bool = ...,
        ignore_case: bool = ...,
    ) -> None: ...
    def compile(self) -> None: ...

class StrMatch(Match):
    def __init__(
        self,
        to_match: str,
        rule_name: str = ...,
        root: bool = ...,
        ignore_case: bool = ...,
    ) -> None: ...

class EndOfFile(Match):
    def __init__(self) -> None: ...

class ParseTreeNode: ...

class PTNodeVisitor(DebugPrinter):
    def __init__(
        self,
        defaults: bool = ...,
        *,
        debug: bool = ...,
    ) -> None: ...

def visit_parse_tree(
    parse_tree: ParseTreeNode, visitor: PTNodeVisitor
) -> Any: ...

class Parser(DebugPrinter):
    ignore_case: bool
    def __init__(
        self,
        skipws: bool = ...,
        ws: str = ...,
        reduce_tree: bool = ...,
        autokwd: bool = ...,
        ignore_case: bool = ...,
        memoization: bool = ...,
        *,
        debug: bool = ...,
    ) -> None: ...
    def parse(self, _input: Any, file_name: Any = ...) -> ParseTreeNode: ...

class CrossRef:
    target_rule_name: str
    def __init__(
        self,
        target_rule_name: str,
        position: int = ...,
    ) -> None: ...

class ParserPython(Parser):
    def __init__(
        self,
        language_def: _ParsingExpressionArgument,
        comment_def: _ParsingExpressionArgument = ...,
        *,
        debug: bool = ...,
        reduce_tree: bool = ...,
        ignore_case: bool = ...,
        memoization: bool = ...,
    ) -> None: ...
