from pathlib import Path


class Workspace:

    def __init__(self):
        self.root = Path.cwd()

    def path(self, relative: str):
        return self.root / relative

    def exists(self, relative: str):
        return self.path(relative).exists()


workspace = Workspace()