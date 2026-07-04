from backend.coding.file_manager import file_manager
from backend.coding.analyzer import analyzer
from backend.coding.patch import patch_manager


class CodeEditor:

    def open(self, path: str):

        code = file_manager.read(path)

        if code is None:
            return None

        return {
            "code": code,
            "analysis": analyzer.analyze(code)
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

    def patch(
        self,
        path: str,
        old: str,
        new: str
    ):

        return patch_manager.replace(
            path,
            old,
            new
        )


editor = CodeEditor()