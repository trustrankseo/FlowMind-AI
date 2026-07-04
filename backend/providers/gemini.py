from google import genai

from backend.config.settings import settings
from backend.providers.base import BaseProvider


class GeminiProvider(BaseProvider):

    def __init__(self):
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)

    async def chat(self, message: str):

        response = self.client.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=message
        )

        return response.text