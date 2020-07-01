
from typing_extensions import Protocol


class SupportsModelicaLiteral(Protocol):
    def __to_literal__(self) -> str:
        ...

    @classmethod
    def __from_literal__(cls, literal: str) -> "SupportsModelicaLiteral":
        ...
