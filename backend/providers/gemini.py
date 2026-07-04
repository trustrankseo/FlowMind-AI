from backend.providers.base import BaseProvider


class GeminiProvider(BaseProvider):

    name = "gemini"

    async def chat(
        self,
        prompt: str
    ):

        # TODO:
        # Real Gemini API Integration

        return "Gemini Response"


gemini_provider = GeminiProvider()