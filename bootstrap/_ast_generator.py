import re
from ast import (
    AnnAssign,
    Attribute,
    Call,
    ClassDef,
    Constant,
    Expr,
    FunctionDef,
    Import,
    ImportFrom,
)
from ast import List as AstList
from ast import Load, Module, Name, Return, Store, Subscript
from ast import Tuple as AstTuple
from ast import alias, arg, arguments, expr, expr_context, keyword, stmt
from dataclasses import dataclass, field
from functools import reduce
from operator import or_
from typing import (
    ClassVar,
    Collection,
    Iterator,
    List,
    Mapping,
    NewType,
    Optional,
    Sequence,
    Set,
    Tuple,
    Union,
)

from arpeggio import (
    EOF,
    NoMatch,
    OneOrMore,
    ParserPython,
    ParseTreeNode,
    PTNodeVisitor,
    RegExMatch,
    Terminal,
    visit_parse_tree,
)
from typing_extensions import Protocol, runtime_checkable

from modelicalang._backend import ParsingExpressionLike

from ._types import Regex, Text


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
    name: str, ctx: Optional[expr_context] = None
) -> Union[Name, Attribute]:
    if ctx is None:
        ctx = Load()
    id, *attrs = name.split(".")
    attribute: Union[Name, Attribute] = Name(id=id, ctx=ctx)
    for attr in attrs:
        attribute = Attribute(value=attribute, attr=attr, ctx=ctx)
    return attribute


def create_call(
    func: str,
    args: Sequence[expr],
) -> Call:
    return Call(
        func=create_attribute(func),
        args=args,
        keywords=[],
    )


def create_constant(
    value: str,
) -> Constant:
    return Constant(value=value, kind=None)


def create_function_def(
    decorator_list: Sequence[str],
    name: str,
    args: Sequence[str],
    returns: str,
    docs: Sequence[str],
    value: expr,
) -> FunctionDef:
    body: List[stmt] = []
    if docs:
        body.append(
            Expr(
                value=create_constant(
                    value="".join(
                        line.rstrip() + "\n" for line in ["", *docs, ""]
                    )
                )
            )
        )
    body.append(Return(value=value))

    return FunctionDef(
        name=name,
        args=arguments(
            posonlyargs=[],
            args=[
                arg(arg=arg_, annotation=None, type_comment=None)
                for arg_ in args
            ],
            vararg=None,
            kwonlyargs=[],
            kw_defaults=[],
            kwarg=None,
            defaults=[],
        ),
        body=body,
        decorator_list=list(map(create_attribute, decorator_list)),
        returns=create_attribute(returns),
        lineno=None,
    )


def create_list(
    elts: Sequence[expr], ctx: Optional[expr_context] = None
) -> AstList:
    if ctx is None:
        ctx = Load()
    return AstList(elts=elts, ctx=ctx)


def create_module_with_class(
    imports: Sequence[str],
    import_froms: Sequence[Tuple[str, Sequence[str]]],
    class_name: str,
    class_bases: Sequence[str],
    class_keywords: Mapping[str, expr],
    class_body: Sequence[stmt],
) -> Module:
    body: List[stmt] = []

    if imports:
        body.append(
            Import(names=[alias(name=name, asname=None) for name in imports])
        )
    if import_froms:
        body.extend(
            [
                ImportFrom(
                    module=module,
                    names=[alias(name=name, asname=None) for name in names],
                    level=0,
                )
                for module, names in import_froms
            ]
        )

    body.append(
        ClassDef(
            name=class_name,
            bases=[create_attribute(class_base) for class_base in class_bases],
            keywords=[
                keyword(arg=arg, value=value)
                for arg, value in class_keywords.items()
            ],
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
    ctx: Optional[expr_context] = None,
) -> Subscript:
    if ctx is None:
        ctx = Load()
    return Subscript(value=value, slice=slice, ctx=ctx)


def create_tuple(
    elts: Sequence[expr], ctx: Optional[expr_context] = None
) -> AstTuple:
    if ctx is None:
        ctx = Load()
    return AstTuple(elts=elts, ctx=ctx)


Pattern = Union[
    Regex,
    "CharacterCodeSet",
    "SupportsPattern",
]

CharacterCode = NewType("CharacterCode", int)
CharacterCodeSet = Set[CharacterCode]


@runtime_checkable
class SupportsPattern(Protocol):
    def resolve(self) -> Pattern:
        ...

    def to_regex(self) -> Regex:
        ...


def resolve_pattern(pattern: Pattern) -> Pattern:
    if isinstance(pattern, (str, set)):
        return pattern
    else:
        return pattern.resolve()


def pattern2regex(pattern: Pattern) -> Regex:
    if isinstance(pattern, str):
        return pattern
    elif isinstance(pattern, set):
        return _character_code_set_to_regex(pattern)
    else:
        return pattern.to_regex()


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
            yield Regex(f"{begin}-{end}")


def _character_code_set() -> ParsingExpressionLike:
    return (
        "[",
        OneOrMore([_character_code_range, _character_code]),
        "]",
        EOF,
    )


def _character_code_range() -> ParsingExpressionLike:
    return _character_code, "-", _character_code


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


@dataclass
class PatternReference:
    target: Optional[Pattern] = field(default=None)

    @property
    def __target(self) -> Pattern:
        assert self.target is not None
        return self.target

    def resolve(self) -> Pattern:
        return resolve_pattern(self.__target)

    def to_regex(self) -> Regex:
        return pattern2regex(self.__target)


@dataclass(frozen=True)
class RepetitionPatternBase:
    pattern: Pattern
    operator: ClassVar[str]

    def resolve(self) -> Pattern:
        return self.__class__(resolve_pattern(self.pattern))

    def to_regex(self) -> Regex:
        return Regex(
            _put_bracket_if(
                pattern2regex(self.pattern),
                isinstance(self.pattern, SequencePatternBase),
            )
            + self.operator
        )


class OptionalPattern(RepetitionPatternBase):
    operator = "?"


class ZeroOrMorePattern(RepetitionPatternBase):
    operator = "*"


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
        return Regex(
            "".join(
                _put_bracket_if(
                    pattern2regex(pattern),
                    isinstance(pattern, OrderedChoicePattern),
                )
                for pattern in self
            )
        )


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
        return Regex("|".join(map(pattern2regex, self)))


def _put_bracket_if(regex: Regex, condition: bool) -> Regex:
    if condition:
        return Regex(rf"({regex})")
    else:
        return regex
