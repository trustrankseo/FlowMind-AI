from fastapi import APIRouter

from backend.deployment.deployer import deployer

router = APIRouter()


@router.post("/run")
async def run_deployment():
    return await deployer.deploy()
