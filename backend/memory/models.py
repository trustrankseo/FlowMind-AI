from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class MemoryItem(BaseModel):
    session_id: str
    category: str
    key: str
    value: str
    created_at: Optional[datetime] = None