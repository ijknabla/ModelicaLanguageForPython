import typing
from ast import (
    Attribute,
    ClassDef,
    Import,
    ImportFrom,
    Load,
    Module,
    Name,
    alias,
    expr,
    stmt,
)


def create_module_with_class(
    imports: typing.Sequence[str],
    import_froms: typing.Sequence[typing.Tuple[str, typing.Sequence[str]]],
    class_name: str,
    class_bases: typing.Sequence[typing.Sequence[str]],
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
            bases=[load_object(*class_base) for class_base in class_bases],
            keywords=[],
            body=class_body,
            decorator_list=[],
        ),
    )

    return Module(
        body=body,
        type_ignores=[],
    )


def load_object(id: str, *attrs: str) -> expr:
    result: expr = Name(id=id, ctx=Load())
    for attr in attrs:
        result = Attribute(value=result, attr=attr, ctx=Load())
    return result
