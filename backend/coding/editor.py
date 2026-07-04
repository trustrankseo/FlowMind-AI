from backend.coding.file_manager import file_manager
from backend.coding.analyzer import analyzer


class CodeEditor:

    def open(
        self,
        path: str
    ):

        code = file_manager.read(path)

        if code is None:
            return None

        analysis = analyzer.analyze(code)

        return {
            "code": code,
            "analysis": analysis
        }

    def save(
        self,
        path: str,
        content: str
    ):

        return file_manager.write(
            path,
            content
        )


editor = CodeEditor()