from backend.providers.base import BaseProvider


class GeminiProvider(BaseProvider):

    async def chat(self, message: str):

        return f"[Gemini] {message}"