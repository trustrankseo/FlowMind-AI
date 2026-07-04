from pydantic import BaseModel


class RepositoryInfo(BaseModel):
    path: str
    total_files: int = 0
    total_folders: int = 0