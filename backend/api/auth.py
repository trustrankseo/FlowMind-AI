from fastapi import APIRouter

from backend.auth.models import LoginRequest
from backend.auth.service import auth_service


router = APIRouter()


@router.post("/login")
async def login(
    request: LoginRequest
):

    return await auth_service.login(
        request.email,
        request.password
    )