from pathlib import Path


class PatchManager:

    def replace(
        self,
        path: str,
        old: str,
        new: str
    ):

        file = Path(path)

        if not file.exists():
            return False

        content = file.read_text(
            encoding="utf-8"
        )

        if old not in content:
            return False

        content = content.replace(
            old,
            new,
            1
        )

        file.write_text(
            content,
            encoding="utf-8"
        )

        return True


patch_manager = PatchManager()