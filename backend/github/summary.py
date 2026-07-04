from backend.github.analyzer import repository_analyzer
from backend.github.scanner import repository_scanner


class RepositorySummary:

    def generate(self, root: str):

        scan = repository_scanner.scan(root)
        analysis = repository_analyzer.analyze(root)

        return {
            "total_files": scan["total_files"],
            "total_folders": scan["total_folders"],
            "extensions": analysis
        }


repository_summary = RepositorySummary()