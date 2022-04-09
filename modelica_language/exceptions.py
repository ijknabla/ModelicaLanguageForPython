class BaseError(Exception):
    ...


class BaseWarning(Warning):
    ...


class SemanticError(BaseError):
    ...


class ParserWarning(BaseWarning):
    ...
