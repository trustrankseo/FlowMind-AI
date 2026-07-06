from google import genai
from google.genai import types

from backend.providers.base import BaseProvider
from backend.config.settings import settings
from backend.core.logger import logger


class GeminiProvider(BaseProvider):

    name = "gemini"

    def __init__(self):

        self._client = None

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

    async def chat(
        self,
        prompt: str
    ):

        try:

            client = self._get_client()

            response = await client.aio.models.generate_content(
                model=settings.GEMINI_MODEL,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=(
                        "You are the FlowMind AI Brain, a helpful "
                        "assistant inside the FlowMind AI backend."
                    )
                )
            )

            return response.text

        except Exception as error:

            logger.error(f"[Gemini] request failed: {error}")

            return (
                "[Gemini error] Could not get a response from Gemini. "
                f"Details: {error}"
            )


gemini_provider = GeminiProvider()