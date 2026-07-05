from backend.coding.file_manager import file_manager


class RefactorEngine:

    def replace(
        self,
        path: str,
        old: str,
        new: str
    ):

        content = file_manager.read(path)

        content = content.replace(
            old,
            new
        )

        file_manager.write(
            path,
            content
        )

        return True


refactor_engine = RefactorEngine()