from fastapi import APIRouter
from pydantic import BaseModel

from backend.images.generator import image_generator

router = APIRouter()


class ImageRequest(BaseModel):
    prompt: str
    number_of_images: int = 1


@router.post("/generate")
async def generate_image(request: ImageRequest):
    return await image_generator.generate(
        request.prompt,
        request.number_of_images
    )
