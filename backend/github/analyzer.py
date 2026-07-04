from pathlib import Path


class RepositoryAnalyzer:

    def analyze(self, root: str):

        extensions = {}

        for file in Path(root).rglob("*.*"):

            ext = file.suffix.lower()

            extensions[ext] = extensions.get(ext, 0) + 1

        return extensions


repository_analyzer = RepositoryAnalyzer()