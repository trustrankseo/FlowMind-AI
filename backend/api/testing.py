from fastapi import APIRouter
from pydantic import BaseModel

from backend.testing.runner import test_runner

router = APIRouter()


class TestRunRequest(BaseModel):
    path: str = "."


@router.post("/run")
async def run_tests(request: TestRunRequest):
    return await test_runner.run(request.path)
