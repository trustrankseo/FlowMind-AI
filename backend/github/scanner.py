from backend.github.tree import repository_tree


class RepositoryScanner:

    def scan(self, root: str):

        tree = repository_tree.scan(root)

        return {
            "total_files": len(tree["files"]),
            "total_folders": len(tree["folders"]),
            "tree": tree
        }


repository_scanner = RepositoryScanner()