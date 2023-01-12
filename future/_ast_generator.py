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


Pattern = Union[
    Regex,
    "CharacterCodeSet",
    "SupportsResolve",
]


CharacterCode = NewType("CharacterCode", int)
CharacterCodeSet = Set[CharacterCode]


@typing.runtime_checkable
class SupportsResolve(Protocol):
    def resolve(self) -> Pattern:
        ...


def regex2pattern(regex: Regex) -> Pattern:
    try:
        return visit_parse_tree(  # type: ignore
            ParserPython(_character_code_set, skipws=False).parse(regex),
            _CharacterCodeSetVisitor(),
        )

    except NoMatch:
        return regex


def text2pattern(text: Text) -> Pattern:
    if len(text) == 1:
        return {CharacterCode(ord(text))}
    else:
        return Regex(re.escape(text))


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

    def to_regex(self) -> Regex:
        return Regex("".join(map(_pattern_to_regex, self)))


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

    def to_regex(self) -> Regex:
        return Regex("".join(map(_pattern_to_regex, self)))


def pattern2regex(pattern: Pattern) -> Regex:
    return _pattern_to_regex(resolve_pattern(pattern))


def resolve_pattern(pattern: Pattern) -> Pattern:
    if isinstance(pattern, (str, set)):
        return pattern
    else:
        return pattern.resolve()


def _pattern_to_regex(pattern: Pattern) -> Regex:
    if isinstance(pattern, str):
        return pattern
    elif isinstance(pattern, set):
        return _character_code_set_to_regex(pattern)
    elif isinstance(pattern, SequencePattern):
        content = "".join(map(_pattern_to_regex, pattern))
        if not root:
            return "(" + content + ")"
        else:
            return content
    elif isinstance(pattern, OrderedChoicePattern):
        content = "|".join(map(_pattern_to_regex, pattern))
        if not root:
            return "(" + content + ")"
        else:
            return content
    elif isinstance(pattern, OptionalPattern):
        return _pattern_to_regex(pattern.pattern) + "?"
    elif isinstance(pattern, ZeroOrMorePattern):
        return _pattern_to_regex(pattern.pattern) + "*"
    raise NotImplementedError()


def _character_code_set_to_regex(
    character_code_set: CharacterCodeSet,
) -> Regex:
    regexs = _character_codes_to_groups(character_code_set)
    if len(character_code_set) == 1:
        (regex,) = regexs
        return regex
    else:
        return Regex(f"[{''.join(regexs)}]")


def _code2regex(code: CharacterCode) -> Regex:
    return Regex(re.escape(chr(code)))


def _character_codes_to_groups(
    items: Collection[CharacterCode],
) -> Iterator[Regex]:
    items = sorted(items)
    partition = [
        i
        for i, (j, k) in enumerate(zip(items[:-1], items[1:]), start=1)
        if j + 1 < k
    ]

    for start, stop in zip(
        [0, *partition],
        [*partition, len(items)],
    ):
        regexs = map(_code2regex, items[start:stop])
        if (stop - start) <= 2:
            yield from regexs
        else:
            begin, *_, end = regexs
            return Regex(f"{begin}-{end}")


@returns_parsing_expression
def _character_code_set() -> ParsingExpressionLike:
    return (
        "[",
        OneOrMore([_character_code_range, _character_code]),
        "]",
        EndOfFile(),
    )


@returns_parsing_expression
def _character_code_range() -> ParsingExpressionLike:
    return _character_code, "-", _character_code


@returns_parsing_expression
def _character_code() -> ParsingExpressionLike:
    return RegExMatch(r"\\.|[^\^\[\]\\]")


class _CharacterCodeSetVisitor(PTNodeVisitor):
    def visit__character_code(
        self, node: Terminal, _: Sequence[CharacterCodeSet]
    ) -> CharacterCodeSet:
        char = re.sub(r"^\\", "", node.value)
        return {CharacterCode(ord(char))}

    def visit__character_code_range(
        self, _: ParseTreeNode, children: Sequence[CharacterCodeSet]
    ) -> CharacterCodeSet:
        (begin,), (end,) = children
        return set(map(CharacterCode, range(begin, end + 1)))

    def visit__character_code_set(
        self, _: ParseTreeNode, children: Sequence[CharacterCodeSet]
    ) -> CharacterCodeSet:
        return reduce(or_, children)
