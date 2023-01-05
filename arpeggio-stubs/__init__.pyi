import typing as _typing

_ParsingExpressionLike__0 = _typing.Union[
    str,
    ParsingExpression,
    _typing.Callable[[], ParsingExpression],
]
_ParsingExpressionLike__1 = _typing.Union[
    _ParsingExpressionLike__0, _typing.Sequence[_ParsingExpressionLike__0]
]
_ParsingExpressionLike__2 = _typing.Union[
    _ParsingExpressionLike__1, _typing.Sequence[_ParsingExpressionLike__1]
]

_ParsingExpressionLike = _ParsingExpressionLike__2

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
        *elements: _ParsingExpressionLike,
        rule_name: str = ...,
        root: bool = ...,
        nodes: _typing.Iterable[ParsingExpression] = ...,
        suppress: bool = ...,
    ) -> None: ...
    root: bool
    rule_name: str
    nodes: _typing.MutableSequence[ParsingExpression]
    @property
    def name(self) -> str: ...
    def parse(self, parser: Parser) -> ParseTreeNode: ...

class Sequence(ParsingExpression): ...
class OrderedChoice(Sequence): ...

class Repetition(ParsingExpression):
    """
    eolterm: _typing.Any
    sep: _typing.Any
    """

    def __init__(
        self,
        *elements: _ParsingExpressionLike,
        rule_name: str = ...,
        root: bool = ...,
        nodes: _typing.Iterable[_ParsingExpressionLike] = ...,
        suppress: bool = ...,
        sep: _ParsingExpressionLike = ...,
    ) -> None: ...
    sep: ParsingExpression | None

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

class Terminal(ParseTreeNode):
    value: str
    def __eq__(self, other: _typing.Any) -> bool: ...

class NonTerminal(ParseTreeNode, _typing.List[ParseTreeNode]): ...

class PTNodeVisitor(DebugPrinter):
    def __init__(
        self,
        defaults: bool = ...,
        *,
        debug: bool = ...,
    ) -> None: ...

def visit_parse_tree(
    parse_tree: ParseTreeNode, visitor: PTNodeVisitor
) -> _typing.Any: ...

class Parser(DebugPrinter):
    ignore_case: bool
    parser_model: ParsingExpression
    comments_model: ParsingExpression | None
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
    def parse(
        self, _input: _typing.Any, file_name: _typing.Any = ...
    ) -> ParseTreeNode: ...

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
        language_def: _ParsingExpressionLike,
        comment_def: _ParsingExpressionLike = ...,
        *,
        debug: bool = ...,
        reduce_tree: bool = ...,
        ignore_case: bool = ...,
        memoization: bool = ...,
    ) -> None: ...
    def _from_python(self, expression: _typing.Any) -> ParsingExpression: ...
