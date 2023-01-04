import os as _os

from . import ParsingExpression

Node = ParsingExpression

class Exporter:
    def exportFile(
        self, obj: Node, file_name: str | _os.PathLike[str]
    ) -> None: ...

class DOTExporter(Exporter): ...
class PMDOTExporter(DOTExporter): ...
