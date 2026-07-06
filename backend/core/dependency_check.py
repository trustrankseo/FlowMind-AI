import importlib


class DependencyCheck:

    required_packages = [
        "fastapi",
        "uvicorn",
        "sqlalchemy",
        "pydantic",
        "jose",
        "passlib",
    ]

    def run(self):

        status = {}

        for package in self.required_packages:

            try:
                importlib.import_module(package)
                status[package] = "ok"

            except ImportError:
                status[package] = "missing"

        return status


dependency_check = DependencyCheck()
