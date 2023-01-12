from ast import Ellipsis, Expr, Module
from typing import Any

from arpeggio import PTNodeVisitor
from typing_extensions import Protocol

from ._ast_generator import create_module_with_class


class SupportsChildren(Protocol):
    ...


class ModuleVisitor(PTNodeVisitor):
    class_name: str

    def __init__(self, class_name: str, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.class_name = class_name

    def visit_grammar(
        self, _: PTNodeVisitor, children: SupportsChildren
    ) -> Module:
        return create_module_with_class(
            imports=[],
            import_froms=[],
            class_name=self.class_name,
            class_bases=[],
            class_body=[Expr(value=Ellipsis())],
        )
