from fastapi import APIRouter
from pydantic import BaseModel

from backend.video.generator import video_generator

router = APIRouter()


class VideoRequest(BaseModel):
    prompt: str


@router.post("/generate")
async def generate_video(request: VideoRequest):
    return await video_generator.generate(request.prompt)
