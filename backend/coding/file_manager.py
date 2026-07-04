from backend.coding.workspace import workspace


class FileManager:

    def read(self, path: str):

        file = workspace.path(path)

        if not file.exists():
            return None

        return file.read_text(
            encoding="utf-8"
        )

    def write(
        self,
        path: str,
        content: str
    ):

        file = workspace.path(path)

        file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        file.write_text(
            content,
            encoding="utf-8"
        )

        return True


file_manager = FileManager()