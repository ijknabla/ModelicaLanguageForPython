import os as _os

from . import ParsingExpression as _ParsingExpression

class Exporter:
    def exportFile(
        self, obj: _ParsingExpression, file_name: str | _os.PathLike[str]
    ) -> None: ...

class DOTExporter(Exporter): ...
class PMDOTExporter(DOTExporter): ...
