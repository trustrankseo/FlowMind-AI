from pathlib import Path


class FileManager:

    def exists(self, path: str):

        return Path(path).exists()

    def read(self, path: str):

        return Path(path).read_text(
            encoding="utf-8"
        )

    def write(
        self,
        path: str,
        content: str
    ):

        Path(path).write_text(
            content,
            encoding="utf-8"
        )

        return True

    def create_folder(
        self,
        path: str
    ):

        Path(path).mkdir(
            parents=True,
            exist_ok=True
        )


file_manager = FileManager()