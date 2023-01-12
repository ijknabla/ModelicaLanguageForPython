from ast import (
    Attribute,
    ClassDef,
    Import,
    ImportFrom,
    Load,
    Module,
    Name,
    alias,
    expr_context,
    stmt,
)
from typing import Optional, Sequence, Union


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


def create_module_with_class(
    imports: Sequence[str],
    import_froms: Sequence["tuple[str, Sequence[str]]"],
    class_name: str,
    class_bases: Sequence[str],
    class_body: Sequence[stmt],
) -> Module:
    body: "list[stmt]" = []

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
