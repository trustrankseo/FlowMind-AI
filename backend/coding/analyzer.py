from pathlib import Path

from backend.coding.ast_parser import ast_parser


class CodeAnalyzer:

    def info(self, path: str):

        file = Path(path)

        if not file.exists():

            return {
                "exists": False
            }

        source = file.read_text(
            encoding="utf-8"
        )

        return {
            "exists": True,
            "name": file.name,
            "suffix": file.suffix,
            "size": file.stat().st_size,
            "functions": ast_parser.functions(source),
            "classes": ast_parser.classes(source)
        }


code_analyzer = CodeAnalyzer()