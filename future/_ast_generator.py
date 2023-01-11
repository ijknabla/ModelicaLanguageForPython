import re
import typing
from ast import (
    AnnAssign,
    Attribute,
    Call,
    ClassDef,
    FunctionDef,
    Import,
    ImportFrom,
    Load,
    Module,
    Name,
    Return,
    Store,
    Subscript,
    Tuple,
    alias,
    arg,
    arguments,
    expr,
    expr_context,
    stmt,
)
from dataclasses import dataclass, field
from functools import reduce
from operator import or_
from typing import (
    Collection,
    Iterator,
    List,
    NewType,
    Optional,
    Protocol,
    Sequence,
    Set,
    Union,
)

from arpeggio import (
    EndOfFile,
    NoMatch,
    OneOrMore,
    ParseTreeNode,
    PTNodeVisitor,
    RegExMatch,
    Terminal,
    visit_parse_tree,
)

from modelica_language import ParserPython

from ._types import (
    ParsingExpressionLike,
    Regex,
    Text,
    returns_parsing_expression,
)


def create_ann_assign(
    target: str,
    annotation: expr,
    value: expr,
) -> AnnAssign:
    return AnnAssign(
        target=create_attribute(target, ctx=Store()),
        annotation=annotation,
        value=value,
        simple=1,
    )


def create_attribute(
    name: str, ctx: typing.Optional[expr_context] = None
) -> typing.Union[Name, Attribute]:
    if ctx is None:
        ctx = Load()
    id, *attrs = name.split(".")
    attribute: typing.Union[Name, Attribute] = Name(id=id, ctx=ctx)
    for attr in attrs:
        attribute = Attribute(value=attribute, attr=attr, ctx=ctx)
    return attribute


def create_call(
    func: str,
    args: typing.Sequence[expr],
) -> Call:
    return Call(
        func=create_attribute(func),
        args=args,
        keywords=[],
    )


def create_function_def(
    name: str,
    args: typing.Sequence[str],
    value: expr,
    decorator_list: typing.Sequence[str],
    returns: str,
) -> FunctionDef:
    return FunctionDef(
        name=name,
        args=arguments(
            posonlyargs=[],
            args=[arg(arg=arg_) for arg_ in args],
            kwonlyargs=[],
            kw_defaults=[],
            defaults=[],
        ),
        body=[Return(value=value)],
        decorator_list=list(map(create_attribute, decorator_list)),
        returns=create_attribute(returns),
        lineno=None,
    )


def create_module_with_class(
    imports: typing.Sequence[str],
    import_froms: typing.Sequence[typing.Tuple[str, typing.Sequence[str]]],
    class_name: str,
    class_bases: typing.Sequence[str],
    class_body: typing.Sequence[stmt],
) -> Module:
    body: typing.List[stmt] = []

    if imports:
        body.append(Import(names=[alias(name=name) for name in imports]))
    if import_froms:
        body.extend(
            [
                ImportFrom(
                    module=module,
                    names=[alias(name=name) for name in names],
                    level=0,
                )
                for module, names in import_froms
            ]
        )

    body.append(
        ClassDef(
            name=class_name,
            bases=[create_attribute(class_base) for class_base in class_bases],
            keywords=[],
            body=class_body,
            decorator_list=[],
        ),
    )

    return Module(
        body=body,
        type_ignores=[],
    )


def create_subscript(
    value: expr,
    slice: expr,
    ctx: typing.Optional[expr_context] = None,
) -> Subscript:
    if ctx is None:
        ctx = Load()
    return Subscript(value=value, slice=slice, ctx=ctx)


def create_tuple(
    elts: typing.Sequence[expr], ctx: typing.Optional[expr_context] = None
) -> Tuple:
    if ctx is None:
        ctx = Load()
    return Tuple(elts=elts, ctx=ctx)


CharacterCode = NewType("CharacterCode", int)
CharacterCodeSet = Set[CharacterCode]


@typing.runtime_checkable
class SupportsResolve(Protocol):
    def resolve(self) -> "Pattern":
        ...


Pattern = Union[
    CharacterCodeSet,
    Regex,
    SupportsResolve,
]


@dataclass
class PatternReference:
    target: Optional[Pattern] = field(default=None)

    def resolve(self) -> Pattern:
        assert self.target is not None
        return resolve_pattern(self.target)


@dataclass(frozen=True)
class RepetitionPatternBase:
    pattern: Pattern


class OptionalPattern(RepetitionPatternBase):
    def resolve(self) -> Pattern:
        return self.__class__(resolve_pattern(self.pattern))


class ZeroOrMorePattern(RepetitionPatternBase):
    def resolve(self) -> Pattern:
        return self.__class__(resolve_pattern(self.pattern))


@dataclass(frozen=True)
class SequencePatternBase:
    patterns: Sequence[Pattern]

    def __iter__(self) -> Iterator[Pattern]:
        yield from self.patterns

    @classmethod
    def _flatten(cls, *patterns: Pattern) -> Iterator[Pattern]:
        if not patterns:
            return

        head, *tail = patterns
        head = resolve_pattern(head)
        if isinstance(head, cls):
            yield from head
        else:
            yield head

        yield from cls._flatten(*tail)


class SequencePattern(SequencePatternBase):
    def resolve(self) -> Pattern:
        head, *tail = self._flatten(*self)
        if tail:
            return SequencePattern((head, *tail))
        else:
            return head


class OrderedChoicePattern(SequencePatternBase):
    def resolve(self) -> Pattern:
        character_code_set: CharacterCodeSet = set()
        patterns: List[Pattern] = []

        for pattern in self._flatten(*self):
            if isinstance(pattern, set):
                character_code_set.update(pattern)
            else:
                patterns.append(pattern)

        if character_code_set:
            patterns.insert(0, character_code_set)

        if len(patterns) == 1:
            return patterns[0]
        else:
            return OrderedChoicePattern(tuple(patterns))


def lexical_text(text: Text) -> Union[CharacterCodeSet, Regex]:
    if len(text) == 1:
        return {CharacterCode(ord(text))}
    else:
        return Regex(re.escape(text))


def lexical_regex(regex: Regex) -> Union[CharacterCodeSet, Regex]:
    try:
        character_code_set: CharacterCodeSet = visit_parse_tree(
            character_set_parser.parse(regex), CharacterSetVisitor()
        )
        return character_code_set
    except NoMatch:
        return Regex(regex)


def to_regex(pattern: Pattern) -> str:
    check_recursion(pattern)
    pattern = resolve_pattern(pattern)
    return _to_regex(pattern, root=True)


def check_recursion(pattern: Pattern) -> None:
    ...


def resolve_pattern(pattern: Pattern) -> Pattern:
    if isinstance(pattern, SupportsResolve):
        return pattern.resolve()
    else:
        return pattern


def _to_regex(pattern: Pattern, root: bool = False) -> str:
    if isinstance(pattern, SequencePattern):
        content = "".join(map(_to_regex, pattern))
        if not root:
            return "(" + content + ")"
        else:
            return content
    elif isinstance(pattern, OrderedChoicePattern):
        content = "|".join(map(_to_regex, pattern))
        if not root:
            return "(" + content + ")"
        else:
            return content
    elif isinstance(pattern, set):
        if len(pattern) == 1:
            (char,) = map(chr, pattern)
            return re.escape(char)
        else:
            groups = []
            for category in categorize(pattern):
                groups.append(
                    "-".join(
                        map(
                            re.escape,
                            map(
                                chr,
                                [category[0]]
                                if len(category) == 1
                                else [category[0], category[-1]],
                            ),
                        )
                    )
                )
            return "[" + "".join(groups) + "]"
    elif isinstance(pattern, str):
        return pattern
    elif isinstance(pattern, OptionalPattern):
        return _to_regex(pattern.pattern) + "?"
    elif isinstance(pattern, ZeroOrMorePattern):
        return _to_regex(pattern.pattern) + "*"
    raise NotImplementedError()


@returns_parsing_expression
def grammar() -> ParsingExpressionLike:
    return "[", OneOrMore(character_set), "]", EndOfFile()


@returns_parsing_expression
def character_set() -> ParsingExpressionLike:
    return [character_range, character]


@returns_parsing_expression
def character() -> ParsingExpressionLike:
    return RegExMatch(r"\\.|[^\^\[\]\\]")


@returns_parsing_expression
def character_range() -> ParsingExpressionLike:
    return character, "-", character


character_set_parser = ParserPython(grammar, skipws=False)


class SupportsChildren(Protocol):
    character: Sequence[CharacterCodeSet]
    character_set: Sequence[CharacterCodeSet]


class CharacterSetVisitor(PTNodeVisitor):
    def visit_character(
        self, node: Terminal, _: SupportsChildren
    ) -> CharacterCodeSet:
        char = re.sub(r"^\\", "", node.value)
        return {CharacterCode(ord(char))}

    def visit_character_range(
        self, _: ParseTreeNode, children: SupportsChildren
    ) -> CharacterCodeSet:
        (begin,), (end,) = children.character
        return set(map(CharacterCode, range(begin, end + 1)))

    def visit_grammar(
        self, _: ParseTreeNode, children: SupportsChildren
    ) -> CharacterCodeSet:
        return reduce(or_, children.character_set)


def categorize(items: Collection[int]) -> Iterator[List[int]]:
    items = sorted(items)
    partition = [
        i
        for i, (j, k) in enumerate(zip(items[:-1], items[1:]), start=1)
        if j + 1 < k
    ]

    for start, stop in zip(
        [0, *partition],
        [*partition, None],
    ):
        yield items[start:stop]
