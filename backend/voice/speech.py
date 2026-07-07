import os
import uuid
import wave

from google import genai
from google.genai import types

from backend.config.settings import settings
from backend.core.logger import logger


class SpeechGenerator:

    def __init__(self, output_dir: str = "generated/audio"):

        self._client = None
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def _get_client(self):

        if self._client is None:

            if not settings.GEMINI_API_KEY:
                raise ValueError(
                    "GEMINI_API_KEY is not set. Add it to your .env file."
                )

            self._client = genai.Client(
                api_key=settings.GEMINI_API_KEY
            )

        return self._client

    async def text_to_speech(self, text: str, voice_name: str = "Kore"):

        try:

            client = self._get_client()

            response = await client.aio.models.generate_content(
                model=settings.GEMINI_TTS_MODEL,
                contents=text,
                config=types.GenerateContentConfig(
                    response_modalities=["AUDIO"],
                    speech_config=types.SpeechConfig(
                        voice_config=types.VoiceConfig(
                            prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                voice_name=voice_name
                            )
                        )
                    )
                )
            )

            audio_data = (
                response.candidates[0]
                .content.parts[0]
                .inline_data.data
            )

            filename = f"{uuid.uuid4().hex}.wav"
            filepath = os.path.join(self.output_dir, filename)

            self._save_wav(filepath, audio_data)

            return {
                "success": True,
                "text": text,
                "audio_path": filepath
            }

        except Exception as error:

            logger.error(f"[SpeechGenerator] request failed: {error}")

            return {
                "success": False,
                "error": f"Text-to-speech failed: {error}"
            }

    def _save_wav(
        self,
        filepath: str,
        pcm_data: bytes,
        channels: int = 1,
        rate: int = 24000,
        sample_width: int = 2
    ):

        with wave.open(filepath, "wb") as wav_file:
            wav_file.setnchannels(channels)
            wav_file.setsampwidth(sample_width)
            wav_file.setframerate(rate)
            wav_file.writeframes(pcm_data)


speech_generator = SpeechGenerator()
