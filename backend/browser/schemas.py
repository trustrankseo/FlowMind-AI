from pydantic import BaseModel


class BrowserRequest(BaseModel):
    action: str
    url: str | None = None
    selector: str | None = None
    text: str | None = None