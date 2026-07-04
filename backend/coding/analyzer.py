class CodeAnalyzer:

    def analyze(
        self,
        code: str
    ):

        lines = len(code.splitlines())

        return {
            "lines": lines,
            "characters": len(code)
        }


analyzer = CodeAnalyzer()