from pydantic import BaseModel
from typing import Optional


class CodeRequest(BaseModel):
    action: str
    file_path: Optional[str] = None
    content: Optional[str] = None