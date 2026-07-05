class CodeFormatter:

    def format(
        self,
        source: str
    ):

        return source.strip() + "\n"


formatter = CodeFormatter()