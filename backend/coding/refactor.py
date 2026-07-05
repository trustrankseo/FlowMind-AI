from backend.coding.file_manager import file_manager
from backend.coding.validator import validator
from backend.coding.formatter import formatter


class RefactorEngine:

    def replace(
        self,
        path: str,
        old: str,
        new: str
    ):

        source = file_manager.read(path)

        updated = source.replace(
            old,
            new
        )

        updated = formatter.format(
            updated
        )

        result = validator.validate(
            updated
        )

        if not result["valid"]:

            return {
                "success": False,
                "error": result["error"]
            }

        file_manager.write(
            path,
            updated
        )

        return {
            "success": True
        }


refactor_engine = RefactorEngine()