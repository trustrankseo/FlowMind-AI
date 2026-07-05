from pathlib import Path


class CodeAnalyzer:

    def info(self, path: str):

        file = Path(path)

        return {
            "name": file.name,
            "suffix": file.suffix,
            "size": file.stat().st_size
            if file.exists()
            else 0,
            "exists": file.exists()
        }


code_analyzer = CodeAnalyzer()