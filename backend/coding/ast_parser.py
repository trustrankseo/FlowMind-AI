import ast


class ASTParser:

    def parse(self, source: str):

        return ast.parse(source)

    def functions(self, source: str):

        tree = self.parse(source)

        return [
            node.name
            for node in ast.walk(tree)
            if isinstance(node, ast.FunctionDef)
        ]

    def classes(self, source: str):

        tree = self.parse(source)

        return [
            node.name
            for node in ast.walk(tree)
            if isinstance(node, ast.ClassDef)
        ]


ast_parser = ASTParser()