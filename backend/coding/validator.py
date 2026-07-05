import ast


class CodeValidator:

    def validate(
        self,
        source: str
    ):

        try:

            ast.parse(source)

            return {
                "valid": True,
                "error": None
            }

        except SyntaxError as e:

            return {
                "valid": False,
                "error": str(e)
            }


validator = CodeValidator()