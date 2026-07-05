from pydantic import BaseModel


class FileRequest(BaseModel):
    path: str


class FileWriteRequest(BaseModel):
    path: str
    content: str