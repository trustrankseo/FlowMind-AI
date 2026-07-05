from backend.coding.editor import editor
from backend.coding.analyzer import code_analyzer


class CodingService:

    def open_file(
        self,
        path: str
    ):

        return {
            "info": code_analyzer.info(path),
            "content": editor.open(path)
        }

    def save_file(
        self,
        path: str,
        content: str
    ):

        editor.save(
            path,
            content
        )

        return {
            "success": True
        }


coding_service = CodingService()