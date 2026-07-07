import os

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

PROJECT_ROOT = os.path.abspath(".")

# Folders we never want to expose in the file explorer.
HIDDEN = {".git", "__pycache__", "node_modules", ".venv", "venv"}


def _safe_path(path: str) -> str:
    """
    Resolves a user-supplied path and guarantees it stays inside the
    project directory. A dashboard visitor (or a chat message routed
    here) should never be able to read or write files outside the
    project — e.g. .env, or anything else on the server.
    """

    resolved = os.path.abspath(os.path.join(PROJECT_ROOT, path))

    if not (resolved == PROJECT_ROOT or resolved.startswith(PROJECT_ROOT + os.sep)):
        raise HTTPException(
            status_code=400,
            detail="Path is outside the project directory."
        )

    return resolved


class SaveFileRequest(BaseModel):
    path: str
    content: str


@router.get("/list")
async def list_directory(path: str = "."):

    target = _safe_path(path)

    if not os.path.isdir(target):
        raise HTTPException(status_code=404, detail="Not a directory.")

    entries = []

    for name in sorted(os.listdir(target)):

        if name in HIDDEN or name.startswith("."):
            continue

        full_path = os.path.join(target, name)

        entries.append({
            "name": name,
            "path": os.path.relpath(full_path, PROJECT_ROOT),
            "is_dir": os.path.isdir(full_path)
        })

    return {"path": os.path.relpath(target, PROJECT_ROOT), "entries": entries}


@router.get("/read")
async def read_file(path: str):

    target = _safe_path(path)

    if not os.path.isfile(target):
        raise HTTPException(status_code=404, detail="File not found.")

    with open(target, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    return {"path": path, "content": content}


@router.post("/save")
async def save_file(request: SaveFileRequest):

    target = _safe_path(request.path)

    with open(target, "w", encoding="utf-8") as f:
        f.write(request.content)

    return {"success": True, "path": request.path}
