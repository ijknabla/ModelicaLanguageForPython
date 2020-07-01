
from typing_extensions import (
    Protocol,
    runtime_checkable
)
import abc


@runtime_checkable
class SupportsModelicaLiteral(Protocol):
    @abc.abstractmethod
    def __to_literal__(self) -> str:
        ...

    @classmethod
    @abc.abstractmethod
    def __from_literal__(cls, literal: str) -> "SupportsModelicaLiteral":
        ...
