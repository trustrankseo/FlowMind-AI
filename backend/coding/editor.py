
from backend.coding.file_manager import file_manager


class CodeEditor:

    def open(
        self,
        path: str
    ):

        return file_manager.read(path)

    def save(
        self,
        path: str,
        content: str
    ):

        file_manager.write(
            path,
            content
        )

        return {
            "success": True
        }


editor = CodeEditor()