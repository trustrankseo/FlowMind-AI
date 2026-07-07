from fastapi import APIRouter
from pydantic import BaseModel

from backend.voice.speech import speech_generator

router = APIRouter()


class SpeechRequest(BaseModel):
    text: str
    voice_name: str = "Kore"


@router.post("/speak")
async def text_to_speech(request: SpeechRequest):
    return await speech_generator.text_to_speech(
        request.text,
        request.voice_name
    )
