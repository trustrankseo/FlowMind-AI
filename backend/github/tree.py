from pathlib import Path


class RepositoryTree:

    def scan(self, root: str):

        root_path = Path(root)

        files = []
        folders = []

        for item in root_path.rglob("*"):

            if item.is_dir():
                folders.append(str(item))

            else:
                files.append(str(item))

        return {
            "files": files,
            "folders": folders
        }


repository_tree = RepositoryTree()