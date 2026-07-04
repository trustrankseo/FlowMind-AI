from pydantic import BaseModel
from typing import Any


class Event(BaseModel):
    name: str
    payload: Any = None