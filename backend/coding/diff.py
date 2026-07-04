import difflib


class DiffManager:

    def compare(
        self,
        old: str,
        new: str
    ):

        return "\n".join(
            difflib.unified_diff(
                old.splitlines(),
                new.splitlines(),
                lineterm=""
            )
        )


diff_manager = DiffManager()