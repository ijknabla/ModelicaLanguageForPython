import typing
from ast import (
    AnnAssign,
    Attribute,
    ClassDef,
    Import,
    ImportFrom,
    Load,
    Module,
    Name,
    Store,
    Subscript,
    Tuple,
    alias,
    expr,
    expr_context,
    stmt,
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
