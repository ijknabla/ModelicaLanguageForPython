
from typing_extensions import (
    Protocol,
    runtime_checkable
)
import abc


@runtime_checkable
class SupportsLiteral(Protocol):
    @abc.abstractmethod
    def __to_literal__(self) -> str:
        ...

    @classmethod
    @abc.abstractmethod
    def __from_literal__(cls, literal: str) -> "SupportsLiteral":
        ...


@runtime_checkable
class SupportsReal(Protocol, SupportsLiteral):
    def __to_literal__(self) -> str:
        return str(float(self))

    @abc.abstractmethod
    def __float__(self) -> float:
        ...


@runtime_checkable
class SupportsInteger(Protocol, SupportsLiteral):
    def __to_literal__(self) -> str:
        return str(int(self))

    @abc.abstractmethod
    def __int__(self) -> int:
        ...


@runtime_checkable
class SupportsBoolean(Protocol, SupportsLiteral):
    def __to_literal__(self) -> str:
        return "true" if self else "false"

    @abc.abstractmethod
    def __bool__(self) -> bool:
        ...
