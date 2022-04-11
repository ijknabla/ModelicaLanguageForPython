import os
from . import ParsingExpression

Node = ParsingExpression

class Exporter:
    def exportFile(
        self, obj: Node, file_name: str | os.PathLike[str]
    ) -> None: ...

class DOTExporter(Exporter): ...
class PMDOTExporter(DOTExporter): ...
