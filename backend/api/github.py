from fastapi import APIRouter

from backend.github.service import github_service

router = APIRouter()


@router.get("/summary")
async def repository_summary():

    return await github_service.summarize(".")